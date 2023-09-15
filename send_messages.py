import requests
from linebot import LineBotApi
from linebot.models import TextSendMessage

def send_telegram_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url)

def send_line_message(token, user_id, message):
    line_bot_api = LineBotApi(token)
    line_bot_api.push_message(user_id, messages=TextSendMessage(text=message))
