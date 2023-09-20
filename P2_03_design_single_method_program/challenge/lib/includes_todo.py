# File: lib/includes_todo.py

def includes_todo(text:str):
    if type(text) != str:
        raise Exception("Error: wrong data type submitted, "
                        "please input text/strings only.")
    if '#TODO' not in text:
        return 'This text does not include a #TODO.'
    return 'This text includes a #TODO.'