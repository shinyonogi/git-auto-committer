import requests
import logging
from linebot import LineBotApi, exceptions
from linebot.models import TextSendMessage
from requests.exceptions import RequestException

from src.utils import get_env_variable

def send_telegram_message(message):
    try:
        telegram_bot_token = get_env_variable('TELEGRAM_BOT_TOKEN')
        telegram_chat_id = get_env_variable('TELEGRAM_CHAT_ID')
        url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_chat_id}&text={message}"
        response = requests.get(url)
        response.raise_for_status()
    except RequestException as e:
        logging.error(f"Telegram API Error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error when sending Telegram message: {e}")


def send_line_message(message):
    try:
        line_channel_access_token = get_env_variable('LINE_CHANNEL_ACCESS_TOKEN')
        line_user_id = get_env_variable('LINE_USER_ID')
        line_bot_api = LineBotApi(line_channel_access_token)
        line_bot_api.push_message(line_user_id, messages=TextSendMessage(text=message))
    except exceptions.LineBotApiError as e:
        logging.error(f"Line API Error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error when sending Line message: {e}")
