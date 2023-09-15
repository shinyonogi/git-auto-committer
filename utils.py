import os

def get_env_use_api(key, default=None):
    value = os.environ.get(key)
    if value is None:
        return False
    return value

def get_env_variable(key, default=None):
    value = os.environ.get(key)
    if value is None:
        raise ValueError(f"{key} is not set in the environment. Please define it in the .env file!")
    return value

def convert_to_hex(n):
    hex_digits = "0123456789ABCDEF"
    return hex_digits[n]
