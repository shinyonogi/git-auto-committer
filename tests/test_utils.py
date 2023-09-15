import pytest
import os

from src.utils import get_env_use_api, get_env_variable, convert_to_hex

def test_get_env_use_api_true():
    os.environ["SAMPLE_KEY"] = "true"
    assert get_env_use_api("SAMPLE_KEY") == True

def test_get_env_use_api_false():
    os.environ["SAMPLE_KEY"] = "false"
    assert get_env_use_api("SAMPLE_KEY") == False

def test_get_env_use_api_invalid_value():
    os.environ["SAMPLE_KEY"] = "maybe"
    with pytest.raises(ValueError):
        get_env_use_api("SAMPLE_KEY")

def test_get_env_variable_exists():
    os.environ["EXISTING_KEY"] = "value"
    assert get_env_variable("EXISTING_KEY") == "value"

def test_get_env_variable_not_exists():
    if "NON_EXISTING_KEY" in os.environ:
        del os.environ["NON_EXISTING_KEY"]
    with pytest.raises(ValueError):
        get_env_variable("NON_EXISTING_KEY")

def test_convert_to_hex_valid():
    assert convert_to_hex(10) == "A"

def test_convert_to_hex_invalid_low():
    with pytest.raises(ValueError):
        convert_to_hex(-1)

def test_convert_to_hex_invalid_high():
    with pytest.raises(ValueError):
        convert_to_hex(16)
