# vue-app/Dockerfile
FROM node:18-alpine

WORKDIR /app

# Copy package.json và package-lock.json
COPY package*.json ./

# Cài đặt các phụ thuộc
RUN npm install

# Copy toàn bộ mã nguồn vào container
COPY . .

# Expose cổng ứng dụng
EXPOSE 5173

# Khởi chạy ứng dụng
CMD ["npm", "run", "dev", "--", "--host"]
