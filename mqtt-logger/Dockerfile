# mqtt-logger/Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy requirements.txt và cài đặt các phụ thuộc
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ mã nguồn vào container
COPY . .

# Expose cổng ứng dụng
EXPOSE 5000

# Khởi chạy ứng dụng
CMD ["python", "mqtt_logger.py"]
