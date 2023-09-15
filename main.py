import random
from dotenv import load_dotenv
import openai
from pathlib import Path

from send_messages import send_line_message
from send_messages import send_telegram_message

from generate_messages import gpt_commit_message_generation

from git_things import git_commit_and_push

from utils import get_env_use_api
from utils import get_env_variable
from utils import convert_to_hex

def main():
    load_dotenv()

    use_openai = get_env_use_api('USE_OPENAI').lower() == 'true'
    use_telegram = get_env_use_api('USE_TELEGRAM').lower() == 'true'
    use_line = get_env_use_api('USE_LINE').lower() == 'true'

    if use_openai:
        openai.api_key = get_env_variable('OPENAI_API_KEY')

    random_address_name = "0x" + "".join([convert_to_hex(random.randint(0, 15)) for _ in range(10)])
    file_name = f"randomAddresses/{random_address_name}"
    Path(file_name).touch()

    for _ in range(random.randint(5, 15)):
        commit_message = gpt_commit_message_generation() if use_openai else "Default Commit Message"

        if use_line:
            send_line_message(commit_message)

        if use_telegram:
            send_telegram_message(commit_message)

        with open(file_name, "a") as file:
            file.write(f"{commit_message}\n")

        git_commit_and_push(commit_message)


if __name__ == "__main__":
    main()
