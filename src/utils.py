import os

def get_env_use_api(key, default=None):
    value = os.environ.get(key)
    print(key, value)
    if value is None:
        return False
    if value.lower() not in ["true", "false"]:
        raise ValueError(f"Invalid value for {key}. Expected 'true' or 'false'.")
    return value == "true"

def get_env_variable(key, default=None):
    value = os.environ.get(key)
    if value is None:
        raise ValueError(f"{key} is not set in the environment. Please define it in the .env file!")
    return value

def convert_to_hex(n):
    if not (0 <= n <= 15):
        raise ValueError(f"Expected an integer between 0 and 15, but got {n}.")
    hex_digits = "0123456789ABCDEF"
    return hex_digits[n]
