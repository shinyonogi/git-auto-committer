import os

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
