from lib.greet import greet

def test_greet_xenia_returns_hello_xenia():
    result = greet("Xenia")
    assert result == "Hello, Xenia!"