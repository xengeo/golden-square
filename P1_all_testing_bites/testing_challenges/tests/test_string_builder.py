# File: test/test_string_builder.py

from lib.string_builder import StringBuilder


def test_reports_initial_empty_string():
    """Test reports empty string initially"""
    string_builder = StringBuilder()
    result = string_builder.output()
    assert result == ""

def test_add_string():
    """Test adds hello to string"""
    string_builder = StringBuilder()
    string_builder.add("hello")
    result = string_builder.output()
    assert result == "hello"

def test_add_two_strings():
    """Test adds two strings"""
    string_builder = StringBuilder()
    string_builder.add("hello")
    string_builder.add(" world")
    result = string_builder.output()
    assert result == "hello world"

def test_correct_string_length():
    """Tests reports string length correctly"""
    string_builder = StringBuilder()
    string_builder.add("hello")
    result = string_builder.size()
    assert result == 5

def test_add_empty_string():
    """Test adds empty string to string"""
    string_builder = StringBuilder()
    string_builder.add("")
    result = string_builder.output()
    assert result == ""

def test_correct_length_empty_string():
    """Test reports length of empty string correctly"""
    string_builder = StringBuilder()
    string_builder.add("")
    result = string_builder.size()
    assert result == 0