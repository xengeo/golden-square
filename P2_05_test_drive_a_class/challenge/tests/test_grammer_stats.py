# standard imports
import pytest

# my imports
from lib.grammer_stat import GrammarStats


"""
If we give a string with correct punctuation.
returns grammar is correct message.
"""
def test_correct_string():
    check_grammar = GrammarStats()
    result = check_grammar.check("Hello World.")
    assert result == True

"""
If we give a string that does not start with a capital, but does have end punctuation.
Returns grammar is not correct message.
"""
def test_start_incorrect_end_correct():
    check_grammar = GrammarStats()
    result = check_grammar.check("hello World.")
    assert result == False

"""
If we give a string that does start with a capital, but does not have correct end punctuation.
Returns grammar is not correct message.
"""
def test_start_correct_end_incorrect():
    check_grammar = GrammarStats()
    result = check_grammar.check("Hello World")
    assert result == False

"""
If we give a string that ends with a '?' and begins with a capital letter.
returns grammar is correct message.
"""
def test_start_correct_end_with_question_mark():
    check_grammar = GrammarStats()
    result = check_grammar.check("Hello World?")
    assert result == True

"""
If we give an empty string.
An error message is returned.
"""
def test_empty_string_gives_error_message():
    check_grammar = GrammarStats()
    with pytest.raises(Exception) as err:
        check_grammar.check("")
    error_message = str(err.value)
    assert error_message == "Cannot verify if grammar is correct if no text is given."
    

"""
After checking one string which is correct
#percentage_good returns 100 
"""
def tests_percentage_good_one_word_good():
    check_grammar = GrammarStats()
    check_grammar.check("Hello.")
    result = check_grammar.percentage_good()
    assert result == 100


"""
Given 2 checks 
1 pass 
1 fail
#percentage_good returns 50 
"""
def tests_percentage_good_two_words_one_good():
    check_grammar = GrammarStats()
    check_grammar.check("Hello.")
    check_grammar.check("Hello")
    result = check_grammar.percentage_good()
    assert result == 50


"""
Given 2 checks 
0 pass 
2 fail
#percentage_good returns 0 
"""
def tests_percentage_good_two_words_zero_good():
    check_grammar = GrammarStats()
    check_grammar.check("Hello")
    check_grammar.check("Hello")
    result = check_grammar.percentage_good()
    assert result == 0


"""
Given 0 checks 
0 pass 
0 fail
#percentage_good returns 0 
"""
def tests_percentage_good_zero_checks_run():
    check_grammar = GrammarStats()
    result = check_grammar.percentage_good()
    assert result == 0