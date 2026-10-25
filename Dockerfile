# Use official lightweight Node.js LTS image
FROM node:20-alpine

# Set working directory
WORKDIR /app

# Copy package specifications
COPY package.json ./

# Install production dependencies
RUN npm install --omit=dev

# Copy application files
COPY server.js ./
COPY english/ ./english/
COPY math/ ./math/
COPY public/ ./public/

# Expose server port
EXPOSE 3000

# Start the application
CMD ["node", "server.js"]
