import paho.mqtt.client as mqtt
import time
import requests

start_time = None

MQTT_BROKER = "192.168.3.140"
PORT = 1883

USERNAME = "admin"
PASSWORD = "YOUR_PASSWORD_HERE"

# Listen to all topics to detect the LED message
TOPIC = "#"

WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbyiYP4wDofdbqnKBBCM5J4pQUpMqFMozvUMw8Ob5ob12_VvjhLF85g7fwULZXCD7QH9FQ/exec"


def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with code:", rc)
    client.subscribe(TOPIC)
    print("Listening to all MQTT topics...")


def on_message(client, userdata, msg):

    global start_time

    message = msg.payload.decode()

    print("Topic:", msg.topic)
    print("Message received:", message)

    # Detect ON message
    if message in ["ON", "1", "true", "True"]:

        start_time = time.time()
        print("LED turned ON")

    # Detect OFF message
    if message in ["OFF", "0", "false", "False"]:

        if start_time is not None:

            end_time = time.time()

            seconds = end_time - start_time
            hours = seconds / 3600

            power = 9
            energy = (power * hours) / 1000

            cost_per_unit = 10
            cost = energy * cost_per_unit

            print("Duration (hours):", hours)
            print("Energy (kWh):", energy)
            print("Cost (₹):", cost)

            data = {
                "device": "LED",
                "hours": hours,
                "energy": energy,
                "cost": cost
            }

            try:
                requests.post(WEBHOOK_URL, json=data)
                print("Data sent to Google Sheets")
            except:
                print("Failed to send data to Google Sheets")


client = mqtt.Client()

client.username_pw_set(USERNAME, PASSWORD)

client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, PORT)

print("Waiting for MQTT messages...")

client.loop_forever()