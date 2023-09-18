# File: test/test_counter.py

from lib.counter import Counter

def test_adds_one_number():
    """Tests add 2 returns 'Counted to 2 so far.'"""
    count = Counter()
    count.add(2)
    result = count.report()
    assert result == "Counted to 2 so far."

def test_adds_two_numbers():
    """Tests add 2 returns 'Counted to 2 so far.'"""
    count = Counter()
    count.add(2)
    count.add(6)
    result = count.report()
    assert result == "Counted to 8 so far."

def test_add_zero():
    """Tests add 0 returns 'Counted to 0 so far.'"""
    count = Counter()
    count.add(0)
    result = count.report()
    assert result == "Counted to 0 so far."

def test_no_add():
    """Tests not adding a number returns 'Counted to 0 so far.'"""
    count = Counter()
    result = count.report()
    assert result == "Counted to 0 so far."

def test_add_negative_num():
    """Tests adding -5 returns 'Counted to -5 so far.'"""
    count = Counter()
    count.add(-5)
    result = count.report()
    assert result == "Counted to -5 so far."