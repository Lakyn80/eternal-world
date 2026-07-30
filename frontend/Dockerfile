FROM node:22-alpine

WORKDIR /app/react-export

COPY react-export/package.json react-export/package-lock.json* ./

RUN npm install

COPY react-export/ ./

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "3000"]
