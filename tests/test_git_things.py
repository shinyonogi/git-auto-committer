import pytest
from unittest.mock import patch

from src.git_things import git_commit_and_push

def test_git_commit_and_push_success():
    with patch('os.system', return_value=0) as mock_system:
        git_commit_and_push("test_message")
        mock_system.assert_any_call("git add .")
        mock_system.assert_any_call('git commit -m "test_message"')
        mock_system.assert_any_call("git push")

def test_git_commit_and_push_fail_add():
    with patch('os.system', side_effect=[1, 0, 0]) as mock_system:
        git_commit_and_push("test_message")
        mock_system.assert_called_with("git add .")

def test_git_commit_and_push_fail_commit():
    with patch('os.system', side_effect=[0, 1, 0]) as mock_system:
        git_commit_and_push("test_message")
        mock_system.assert_any_call('git commit -m "test_message"')

def test_git_commit_and_push_fail_push():
    with patch('os.system', side_effect=[0, 0, 1]) as mock_system:
        git_commit_and_push("test_message")
        mock_system.assert_any_call("git push")
