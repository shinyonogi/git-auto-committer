import os
import random
from dotenv import load_dotenv
import openai
from pathlib import Path

from send_messages import send_line_message
from send_messages import send_telegram_message

from generate_messages import commit_message_generation

from utils import get_env_variable
from utils import convert_to_hex

def main():
    load_dotenv()
    openai.api_key = get_env_variable('OPENAI_API_KEY')
    telegram_bot_token = get_env_variable('TELEGRAM_BOT_TOKEN')
    telegram_chat_id = get_env_variable('TELEGRAM_CHAT_ID')
    line_channel_access_token = get_env_variable('LINE_CHANNEL_ACCESS_TOKEN')
    line_user_id = get_env_variable('LINE_USER_ID')

    random_address_name = "0x" + "".join([convert_to_hex(random.randint(0, 15)) for _ in range(10)])
    file_name = f"randomAddresses/{random_address_name}"
    Path(file_name).touch()

    for _ in range(random.randint(5, 15)):
        commit_message = commit_message_generation()

        with open(file_name, "a") as file:
            file.write(f"{commit_message}\n")

        send_telegram_message(telegram_bot_token, telegram_chat_id, commit_message)
        send_line_message(line_channel_access_token, line_user_id, commit_message)

        os.system("git add .")
        os.system(f'git commit -m "{commit_message}"')

    os.system("git push")


if __name__ == "__main__":
    main()
