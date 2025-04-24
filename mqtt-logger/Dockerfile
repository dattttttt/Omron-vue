# mqtt-logger/Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install flask paho-mqtt flask-cors

EXPOSE 5000
CMD ["python", "app.py"]
