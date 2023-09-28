# File: tests/test_secret_diary.py

# standard imports
import pytest
from unittest.mock import Mock

# codebase imports
from lib.secret_diary import SecretDiary


"""
Given a diary, secret diary intialises a secret diary object
which starts off locked
#read returns: Error "Go away!"
"""
def test_secret_diary_initially_locked_read_raises_error():
    
    mock_diary = Mock()
    my_secret_diary = SecretDiary(mock_diary)

    with pytest.raises(Exception) as err:
        my_secret_diary.read()

    assert str(err.value) == "Go away!"
    

"""
After unlocking secret diary
#read returns contents
"""
def test_unlocked_secret_diary_read_returns_contents():
    
    mock_diary = Mock()
    mock_diary.read.return_value = "This is my contents"

    my_secret_diary = SecretDiary(mock_diary)
    my_secret_diary.unlock()

    assert my_secret_diary.read() == "This is my contents"
    mock_diary.read.assert_called()


"""
After unlocking secret diary, then locking again
#read raises error message
"""
def test_unlocked_then_locked_secret_diary_read_returns_contents():
    
    mock_diary = Mock()
    mock_diary.read.return_value = "This is my contents"

    my_secret_diary = SecretDiary(mock_diary)

    # unlock
    my_secret_diary.unlock()
    assert my_secret_diary.read() == "This is my contents"

    # lock again
    my_secret_diary.lock()
    with pytest.raises(Exception) as err:
        my_secret_diary.read()
    assert str(err.value) == "Go away!"