import pytest
from unittest.mock import patch, Mock

from src.send_messages import send_telegram_message, send_line_message

def mock_telegram_response():
    class Response:
        status_code = 200

        @staticmethod
        def raise_for_status():
            pass

    return Response()

def test_send_telegram_message_success(mocker):
    mocker.patch('requests.get', return_value=mock_telegram_response())

    send_telegram_message("Test message")


def test_send_telegram_message_api_error(mocker):
    mocker.patch('requests.get', side_effect=Exception("API Error"))

    send_telegram_message("Test message")


def test_send_line_message_success(mocker):
    mocker.patch('linebot.LineBotApi.push_message')

    send_line_message("Test message")

def test_send_line_message_api_error(mocker):
    mocker.patch('linebot.LineBotApi.push_message', side_effect=Exception("API Error"))

    send_line_message("Test message")
