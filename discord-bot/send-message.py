# pip install requests

import requests

token = ""

def send_message(kanalid, mesaj):
    url = f"https://discord.com/api/v9/channels/{kanalid}/messages"
    headers = {
        "Authorization": f"Bot {token}",
        "Content-Type": "application/json"
    }
    data = {
        "content": mesaj
    }
    r = requests.post(url, headers=headers, json=data)
    if r.status_code == 200:
        print("Message sent")
    else:
        print("Error:", r.status_code)

kanal = input("Channel ID: ")

while True:
    mesaj = input("Message: ")
    if mesaj.lower() == 'q':
        channel_id = input("Channel ID: ")
        continue
    send_message(kanal, mesaj)