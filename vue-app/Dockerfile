# vue-app/Dockerfile
FROM node:18-alpine

WORKDIR /app

# 🟢 Copy thêm file .env vào container
COPY .env .                       

# Chỉ copy file cấu hình trước để cài npm
COPY package*.json ./
RUN npm install

# Copy phần còn lại của dự án
COPY . .

EXPOSE 5173
CMD ["npm", "run", "dev", "--", "--host"]
