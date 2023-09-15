import os
import io
from dotenv import load_dotenv
import random
from pathlib import Path
import openai
import requests
from linebot import LineBotApi
from linebot.models import TextSendMessage

from utils import get_env_variable
from utils import convert_to_hex
from utils import commit_message_generation

def main():
    load_dotenv()
    openai_api_key = get_env_variable('OPENAI_API_KEY')
    telegram_bot_token = get_env_variable('TELEGRAM_BOT_TOKEN')
    telegram_chat_id = get_env_variable('TELEGRAM_CHAT_ID')
    line_channel_access_token = get_env_variable('LINE_CHANNEL_ACCESS_TOKEN')
    line_user_id = get_env_variable('LINE_USER_ID')

    openai.api_key = openai_api_key
    line_bot_api = LineBotApi(line_channel_access_token)

    buffer = io.StringIO()
    for i in range(10):
        buffer.write(str(convert_to_hex(random.randint(0, 15))))
    random_address_name = f"0x{buffer.getvalue()}"
    buffer.close()
    file_name = f"randomAddresses/{random_address_name}"
    Path(file_name).touch()

    for today_contribution_number in range(random.randint(5, 15)):
        commit_message = commit_message_generation()

        file = open(file_name, "a")
        file.write(f"{commit_message}\n")
        file.close()

        telegram_url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_chat_id}&text={commit_message}"
        requests.get(telegram_url)

        line_bot_api.push_message(line_user_id, messages=TextSendMessage(text=commit_message))

        os.system("git add .")
        os.system(f"git commit -m '{commit_message}'")

    os.system("git push")


if __name__ == "__main__":
    main()
