# File: test/test_integration.py

import pytest

from lib.diary import Diary
from lib.secret_diary import SecretDiary

"""
Test real diary instance can be read after unlock
and raises error if attempt to read after locking
"""
def test_diary_instance_read_then_raises_error_after_unlock_then_relock():
    
    diary_entry = Diary('This is my diary...')
    secret_diary = SecretDiary(diary_entry)

    secret_diary.unlock()
    assert secret_diary.read() == 'This is my diary...'

    secret_diary.lock()
    with pytest.raises(Exception) as err:
        secret_diary.read()
    assert str(err.value) == "Go away!"