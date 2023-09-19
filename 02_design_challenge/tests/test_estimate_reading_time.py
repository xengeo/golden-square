# File: test/test_estimate_reading_time.py
from lib.estimate_reading_time import estimate_reading_time
import pytest


"""
Given a string of 200 words
Returns: "This text will take 1 mins to read"
"""

def test_reading_time_200_words():
    text = ' '.join('word' for i in range(0,200))
    results = estimate_reading_time(text)
    assert results == 'This text will take 1.0 mins to read'



"""
Given a string of 300 words
Returns: "This text will take 1.5 mins to read"
"""

def test_reading_time_300_words():
    text = ' '.join('word' for i in range(0,300))
    results = estimate_reading_time(text)
    assert results == "This text will take 1.5 mins to read"



"""
Given a string of 400 words
Returns: "This text will take 1.5 mins to read"
"""

def test_reading_time_400_words():
    text = ' '.join('word' for i in range(0,400))
    results = estimate_reading_time(text)
    assert results == "This text will take 2.0 mins to read"




"""
Given an empty string
Returns: "Cannot give estimate of reading time if no text is given."
"""

def test_reading_time_empty_string():
    with pytest.raises(Exception) as err:
        estimate_reading_time('')
    error_message = str(err.value)
    assert error_message == "Cannot give estimate of reading time if no text is given."


"""
Given a 5 word string
Returns: "This text will take 0.025 mins to read"
"""

def test_reading_time_5_words():
    text = ' '.join('word' for i in range(0, 5))
    results = estimate_reading_time(text)
    assert results == "This text will take 0.025 mins to read"
    