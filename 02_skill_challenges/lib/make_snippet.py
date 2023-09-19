# File: lib/make_snippet.py

def make_snippet(text):

    words_list = text.split(' ')
    if len(words_list) > 5:
        first_five = words_list[:5]
        snippet = ' '.join(first_five)
        return snippet + '...'
    else:
        return text