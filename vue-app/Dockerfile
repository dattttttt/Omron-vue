# vue-app/Dockerfile
FROM node:18-slim

WORKDIR /app

# ✅ Copy file cấu hình dependency
COPY package*.json ./

# ✅ Cài thư viện đúng bên trong container
RUN npm install

# ✅ Copy phần còn lại của code
COPY . .

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "5173"]
