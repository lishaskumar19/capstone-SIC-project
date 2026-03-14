import paho.mqtt.client as mqtt
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "credentials.json", scope)

client = gspread.authorize(creds)

sheet = client.open("SmartHostelEnergy").sheet1



def on_message(client, userdata, msg):

    payload = msg.payload.decode()
    print("Received MQTT:", payload)
        data = payload.split(",")

    energy = data[0]
    cost = data[1]

    sheet.append_row([energy, cost])

mqtt_client = mqtt.Client()

mqtt_client.connect("localhost",1883)

mqtt_client.subscribe("r1/l1/data")

mqtt_client.on_message = on_message

mqtt_client.loop_forever()
