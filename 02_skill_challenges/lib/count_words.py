# File: lib/count_words.py

def count_words(string:str):

    if string:
        words = string.split(' ')
        number_of_words = len(words)
        return number_of_words
    return 0