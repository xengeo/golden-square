# File: tests/test_password_checker.py
import pytest
from lib.password_checker import PasswordChecker


def test_correct_password_length():
    """Test password >= 8 returns True."""
    password = PasswordChecker()
    assert password.check('password1234') == True


def test_invalid_password():
    """Tests a short password returns error message."""
    password = PasswordChecker()
    with pytest.raises(Exception) as err:
        password.check('123')
    error_message = str(err.value)
    assert error_message == "Invalid password, must be 8+ characters."