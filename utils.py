import os
import openai

def get_env_variable(key, default=None):
    value = os.environ.get(key)
    if value is None:
        raise ValueError(f"{key} is not set in the environment")
    return value

def convert_to_hex(n):
    if 0 <= n <= 15:
        hex_digits = "0123456789ABCDEF"
        return hex_digits[n]
    else:
        return 'error occured'

def commit_message_generation():
    content = f"""
    Give me an interesting random fact in one sentence.
    """
    message = [{"role": "user", "content": content}]

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo-0301",
        messages = message
    )
    return response.choices[0].message.content
