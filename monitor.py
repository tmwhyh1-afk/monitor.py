import requests
from bs4 import BeautifulSoup
import os

BOT_TOKEN = os.getenv("8792686474:AAFmWTm7If7pDpHy0_8M3cJT1YvlyO5RZjI")
CHAT_ID = os.getenv("5951518400")

URL = "https://tl.logisty-iq.com"

SAVE_FILE = "data.txt"

def send(msg):
    api = f"https://api.telegram.org/bot{8792686474:AAFmWTm7If7pDpHy0_8M3cJT1YvlyO5RZjI}/sendMessage"
    requests.post(api, data={
        "chat_id": 5951518400,
        "text": msg
    })

response = requests.get(URL, timeout=30)
html = response.text

soup = BeautifulSoup(html, "html.parser")

numbers = []

for item in soup.find_all():
    text = item.get_text(strip=True)

    if "د.ع" in text or "$" in text:
        numbers.append(text)

current = "\n".join(numbers)

old = ""

if os.path.exists(SAVE_FILE):
    with open(SAVE_FILE, "r", encoding="utf-8") as f:
        old = f.read()

if current != old:
    send("تم تغير البيانات:\n\n" + current)

    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        f.write(current)
