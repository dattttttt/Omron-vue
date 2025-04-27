# mqtt-logger/app.py
from flask import Flask, jsonify
import paho.mqtt.client as mqtt
import json, csv, os
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])
CSV_FILE = 'sensor_data.csv'
BROKER = 'mosquitto'
PORT = 1883
TOPIC = 'CPS/data'

# Tạo file CSV nếu chưa có
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Tên cảm biến', 'Giá trị', 'Thời gian'])

# MQTT callbacks
def on_connect(client, userdata, flags, rc):
    print("✅ Connected to MQTT")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if 'DATA' in payload:
            for item in payload['DATA']:
                name = item.get('NE', 'Unknown')
                value = item.get('V', '')
                with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
                    csv.writer(f).writerow([name, value, timestamp])
                print(f"📥 {name}, {value}, {timestamp}")
    except Exception as e:
        print(f"❌ Error: {e}")

# Flask API
@app.route('/api/data', methods=['GET'])
def get_csv_data():
    with open(CSV_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return jsonify(lines[-20:])  # trả về 20 dòng mới nhất

# Khởi động MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT, 60)
client.loop_start()

# Chạy Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
