import paho.mqtt.client as mqtt
import json
import csv
from datetime import datetime
import os

BROKER = 'localhost'
PORT = 9001
TOPIC = 'CPS/data'
CSV_FILE = 'sensor_data.csv'

# Nếu chưa có file, tạo header
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Tên cảm biến', 'Giá trị', 'Thời gian'])

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to MQTT Broker via WebSocket!")
        client.subscribe(TOPIC)
    else:
        print(f"❌ Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode()
        data = json.loads(payload)

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if 'DATA' in data:
            for entry in data['DATA']:
                name = entry.get('NE', 'Unknown')
                value = entry.get('V', '')
                with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow([name, value, timestamp])
                print(f"📥 Đã ghi: {name}, {value}, {timestamp}")
        else:
            print("⚠️ Không có trường 'DATA' trong payload.")

    except Exception as e:
        print(f"❌ Lỗi xử lý message: {e}")

client = mqtt.Client(transport="websockets")
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
print(f"🚀 Đang lắng nghe topic '{TOPIC}'...\n")
client.loop_forever()
