from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8146135748:AAH2YS5MKGAHOksbBRnjMKyWQflP3Ypm7nw"
CHAT_ID = "519458729"  # بعداً جایگزین می‌کنیم

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    message = data.get('message', 'No message received!')
    send_to_telegram(message)
    return 'OK'

def send_to_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": msg
    }
    requests.post(url, json=payload)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
