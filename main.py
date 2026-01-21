from fastapi import FastAPI
from pydantic import BaseModel
import json
import paho.mqtt.client as mqtt
import time
import os

MQTT_BROKER = os.getenv("MQTT_BROKER", "192.168.0.32")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_TOPIC = os.getenv("MQTT_TOPIC", "factory/process/status")

app = FastAPI()

class ProcessStatus(BaseModel):
    process_status: int

def on_connect(client, userdata, flags, rc):
    print(f"MQTT connected with result code {rc}")

def on_disconnect(client, userdata, rc):
    print("MQTT disconnected, reconnecting...")
    while True:
        try:
            client.reconnect()
            break
        except:
            time.sleep(5)

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_disconnect = on_disconnect
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
mqtt_client.loop_start()

@app.post("/process-status")
def send_process_status(data: ProcessStatus):
    payload = json.dumps(data.dict())
    result = mqtt_client.publish(MQTT_TOPIC, payload)

    return {
        "mqtt_publish_rc": result.rc,
        "topic": MQTT_TOPIC,
        "data": data
    }
