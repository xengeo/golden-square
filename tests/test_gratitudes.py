#  File: tests/test_gratitudes.py
from lib.gratitudes import Gratitudes



def test_not_adding_gratitudes():
    """
    Tests not adding gratitude 
    returns start of formatted sentence
    """
    gratitudes = Gratitudes()
    result = gratitudes.format()
    assert result == "Be grateful for: "


def test_add_multiple_gratitudes():
    """
    Tests adding multiple gratitudes
    returns correctly formatted sentence
    """
    gratitudes = Gratitudes()
    gratitudes.add("family")
    gratitudes.add("friends")
    result = gratitudes.format()
    assert result == "Be grateful for: family, friends"

def test_adding_blank_gratitude():
    """Not really how it would be used"""
    gratitudes = Gratitudes()
    gratitudes.add(" ")
    result = gratitudes.format()
    assert result == "Be grateful for:  "