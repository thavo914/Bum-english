import express from 'express';
import http from 'http';
import { WebSocketServer, WebSocket } from 'ws';
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';
import dotenv from 'dotenv';
import { GoogleGenAI } from '@google/genai';
import { marked } from 'marked';

dotenv.config();

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const server = http.createServer(app);
const wss = new WebSocketServer({ server });

const PORT = process.env.PORT || 3000;
const GEMINI_API_KEY = process.env.GEMINI_API_KEY;

app.use(express.static(path.join(__dirname, 'public')));
app.use(express.json());

// API: List lessons
app.get('/api/weeks', (req, res) => {
  const lessonsDir = path.join(__dirname, 'lessons');
  if (!fs.existsSync(lessonsDir)) {
    return res.json([]);
  }
  const weeks = fs.readdirSync(lessonsDir).filter(f => fs.statSync(path.join(lessonsDir, f)).isDirectory());
  const data = weeks.map(week => {
    const weekPath = path.join(lessonsDir, week);
    const days = fs.readdirSync(weekPath).filter(f => fs.statSync(path.join(weekPath, f)).isDirectory());
    return { week, days };
  });
  res.json(data);
});

// Markdown viewer route
app.get('/lessons/:week/:day/:file', (req, res) => {
  const filePath = path.join(__dirname, 'lessons', req.params.week, req.params.day, req.params.file);
  if (!fs.existsSync(filePath)) {
    return res.status(404).send('File not found');
  }
  const mdContent = fs.readFileSync(filePath, 'utf-8');
  const htmlContent = marked.parse(mdContent);
  res.send(`
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>${req.params.file} - Nephew English</title>
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.5.1/github-markdown-dark.min.css">
      <style>
        body {
          background-color: #0d1117;
          color: #c9d1d9;
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
          padding: 20px;
          max-width: 860px;
          margin: 0 auto;
        }
        .nav-back {
          margin-bottom: 20px;
        }
        .nav-back a {
          color: #58a6ff;
          text-decoration: none;
          font-weight: bold;
        }
        .markdown-body {
          background-color: transparent !important;
        }
      </style>
    </head>
    <body>
      <div class="nav-back"><a href="/">← Back to Dashboard</a></div>
      <article class="markdown-body">
        ${htmlContent}
      </article>
    </body>
    </html>
  `);
});

// Gemini Live WebSocket bridge for Buddy Leo
wss.on('connection', async (ws, req) => {
  if (req.url === '/live') {
    if (!GEMINI_API_KEY) {
      ws.send(JSON.stringify({ error: 'GEMINI_API_KEY is not configured.' }));
      ws.close();
      return;
    }
    try {
      const ai = new GoogleGenAI({ apiKey: GEMINI_API_KEY });
      const session = await ai.aio.liveStream({
        model: 'models/gemini-2.0-flash-exp',
        config: {
          generationConfig: {
            responseModalities: ['AUDIO'],
            speechConfig: {
              voiceConfig: {
                prebuiltVoiceConfig: { voiceName: 'Aoede' }
              }
            }
          },
          systemInstruction: {
            parts: [{
              text: "You are 'Leo', an enthusiastic, friendly 15-year-old English speaking buddy for a 14-year-old student. You speak simple, natural, clear English at CEFR A1-A2 level. You love games, tech, and school hobbies. Keep your sentences short (under 12 words). Praise good effort and ask easy follow-up questions."
            }]
          }
        }
      });

      (async () => {
        try {
          for await (const message of session.receive()) {
            if (ws.readyState === WebSocket.OPEN) {
              ws.send(JSON.stringify(message));
            }
          }
        } catch (err) {
          console.error('Session receive error:', err);
        }
      })();

      ws.on('message', async (data) => {
        try {
          const clientMsg = JSON.parse(data.toString());
          await session.send(clientMsg);
        } catch (err) {
          console.error('Session send error:', err);
        }
      });

      ws.on('close', () => {
        session.close();
      });
    } catch (e) {
      console.error('Failed to establish Gemini Live session:', e);
      ws.close();
    }
  }
});

server.listen(PORT, () => {
  console.log(`Nephew English Hub running on http://localhost:${PORT}`);
});
