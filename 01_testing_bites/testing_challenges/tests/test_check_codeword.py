from lib.check_codeword import check_codeword


def test_with_correct_codeword():
    """If the codeword is correct, returns 'Correct! Come in.'"""

    result = check_codeword("horse")
    assert result == "Correct! Come in."


def test_with_close_codeword():
    """If the codeword is close, returns 'Close, but nope.'"""
    
    result = check_codeword("house")
    assert result == "Close, but nope."


def test_with_incorrect_codeword():
    """If the codeword is wrong, returns 'WRONG!'"""

    result = check_codeword("chicken")
    assert result == "WRONG!"