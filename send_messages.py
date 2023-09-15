import requests
from linebot import LineBotApi
from linebot.models import TextSendMessage

from utils import get_env_variable

def send_telegram_message(message):
    telegram_bot_token = get_env_variable('TELEGRAM_BOT_TOKEN')
    telegram_chat_id = get_env_variable('TELEGRAM_CHAT_ID')
    url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_chat_id}&text={message}"
    requests.get(url)

def send_line_message(message):
    line_channel_access_token = get_env_variable('LINE_CHANNEL_ACCESS_TOKEN')
    line_user_id = get_env_variable('LINE_USER_ID')
    line_bot_api = LineBotApi(line_channel_access_token)
    line_bot_api.push_message(line_user_id, messages=TextSendMessage(text=message))
