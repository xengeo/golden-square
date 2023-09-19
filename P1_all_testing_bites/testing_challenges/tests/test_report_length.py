from lib.report_length import report_length

def test_correct_length():
    """Tests correct length returns 'This string was 5 characters long'"""
    result = report_length('hello')
    assert result == 'This string was 5 characters long'

def test_empty_string():
    """Tests empty string returns 'This string was 0 characters long'"""
    result = report_length('')
    assert  result == 'This string was 0 characters long'
    
def test_string_with_whitespace_on_both_ends():
    """Tests a string with whitespace at both ends."""
    result = report_length('  Hello  ')
    assert  result == 'This string was 9 characters long'