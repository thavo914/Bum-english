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

// Helper: Scan lessons folder
function getWeeksForSubject(subject) {
  const lessonsDir = path.join(__dirname, subject, 'lessons');
  if (!fs.existsSync(lessonsDir)) {
    // Fallback if legacy folder still exists
    const legacyDir = path.join(__dirname, 'lessons');
    if (subject === 'english' && fs.existsSync(legacyDir)) {
      const weeks = fs.readdirSync(legacyDir).filter(f => fs.statSync(path.join(legacyDir, f)).isDirectory());
      return weeks.map(week => {
        const weekPath = path.join(legacyDir, week);
        const days = fs.readdirSync(weekPath).filter(f => fs.statSync(path.join(weekPath, f)).isDirectory());
        return { week, days };
      });
    }
    return [];
  }
  const weeks = fs.readdirSync(lessonsDir).filter(f => fs.statSync(path.join(lessonsDir, f)).isDirectory());
  return weeks.map(week => {
    const weekPath = path.join(lessonsDir, week);
    const days = fs.readdirSync(weekPath).filter(f => fs.statSync(path.join(weekPath, f)).isDirectory());
    return { week, days };
  });
}

// API: Multi-subject catalog
app.get('/api/subjects', (req, res) => {
  const englishWeeks = getWeeksForSubject('english');
  const mathWeeks = getWeeksForSubject('math');

  // Math Topics
  const mathTopicsDir = path.join(__dirname, 'math', 'topics');
  let mathTopics = [];
  if (fs.existsSync(mathTopicsDir)) {
    mathTopics = fs.readdirSync(mathTopicsDir)
      .filter(f => fs.statSync(path.join(mathTopicsDir, f)).isDirectory())
      .map(t => {
        const readmePath = path.join(mathTopicsDir, t, 'README.md');
        let title = t;
        if (fs.existsSync(readmePath)) {
          const firstLine = fs.readFileSync(readmePath, 'utf-8').split('\n')[0];
          title = firstLine.replace(/^#\s*/, '').trim() || t;
        }
        return { slug: t, title };
      });
  }

  // Math Cheatsheets
  const cheatsheetsDir = path.join(__dirname, 'math', 'cheatsheets');
  let mathCheatsheets = [];
  if (fs.existsSync(cheatsheetsDir)) {
    mathCheatsheets = fs.readdirSync(cheatsheetsDir)
      .filter(f => f.endsWith('.md'))
      .map(f => ({
        filename: f,
        name: f.replace('.md', '').replace(/-/g, ' ')
      }));
  }

  res.json({
    english: {
      name: "Tiếng Anh (CEFR A1–A2)",
      weeks: englishWeeks
    },
    math: {
      name: "Toán Học (Lớp 9 & Vào 10)",
      weeks: mathWeeks,
      topics: mathTopics,
      cheatsheets: mathCheatsheets
    }
  });
});

// API: Subject-specific weeks
app.get('/api/:subject/weeks', (req, res) => {
  res.json(getWeeksForSubject(req.params.subject));
});

// Backward-compatible API
app.get('/api/weeks', (req, res) => {
  res.json(getWeeksForSubject('english'));
});

// Helper: Render markdown document with MathJax & GitHub dark theme
function renderMarkdownPage(res, title, mdContent) {
  const htmlContent = marked.parse(mdContent);
  res.send(`
    <!DOCTYPE html>
    <html lang="vi">
    <head>
      <meta charset="UTF-8">
      <title>${title} - Bum Study Hub</title>
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.5.1/github-markdown-dark.min.css">
      <style>
        body {
          background-color: #0d1117;
          color: #c9d1d9;
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
          padding: 20px;
          max-width: 900px;
          margin: 0 auto;
        }
        .nav-back {
          margin-bottom: 24px;
          display: flex;
          align-items: center;
          gap: 12px;
        }
        .nav-back a {
          color: #58a6ff;
          text-decoration: none;
          font-weight: 600;
          padding: 6px 14px;
          background: #161b22;
          border: 1px solid #30363d;
          border-radius: 6px;
          transition: all 0.2s;
        }
        .nav-back a:hover {
          background: #1f242c;
          border-color: #58a6ff;
        }
        .markdown-body {
          background-color: transparent !important;
          line-height: 1.65;
        }
        details summary {
          cursor: pointer;
          font-weight: 600;
          color: #58a6ff;
        }
      </style>
      <script>
        window.MathJax = {
          tex: {
            inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
            displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']]
          }
        };
      </script>
      <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" id="MathJax-script" async></script>
    </head>
    <body>
      <div class="nav-back">
        <a href="/">← Trở Về Dashboard</a>
      </div>
      <article class="markdown-body">
        ${htmlContent}
      </article>
    </body>
    </html>
  `);
}

// Subject-scoped lesson viewer route
app.get('/lessons/:subject/:week/:day/:file', (req, res) => {
  const filePath = path.join(__dirname, req.params.subject, 'lessons', req.params.week, req.params.day, req.params.file);
  if (!fs.existsSync(filePath)) {
    return res.status(404).send('File not found: ' + filePath);
  }
  const mdContent = fs.readFileSync(filePath, 'utf-8');
  renderMarkdownPage(res, req.params.file, mdContent);
});

// General Markdown Viewer for topics, cheatsheets, assessments, and exams
app.get('/view/:subject/*', (req, res) => {
  const relPath = req.params[0];
  const filePath = path.join(__dirname, req.params.subject, relPath);
  if (!fs.existsSync(filePath) || !fs.statSync(filePath).isFile()) {
    return res.status(404).send('File not found: ' + filePath);
  }
  const mdContent = fs.readFileSync(filePath, 'utf-8');
  renderMarkdownPage(res, path.basename(filePath), mdContent);
});

// Backward-compatible lesson viewer route for english
app.get('/lessons/:week/:day/:file', (req, res) => {
  let filePath = path.join(__dirname, 'english', 'lessons', req.params.week, req.params.day, req.params.file);
  if (!fs.existsSync(filePath)) {
    filePath = path.join(__dirname, 'lessons', req.params.week, req.params.day, req.params.file);
  }
  if (!fs.existsSync(filePath)) {
    return res.status(404).send('File not found');
  }
  const mdContent = fs.readFileSync(filePath, 'utf-8');
  renderMarkdownPage(res, req.params.file, mdContent);
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
  console.log(`Bum Study Hub running on http://localhost:${PORT}`);
});
