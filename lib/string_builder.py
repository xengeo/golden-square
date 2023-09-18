# File: lib/string_builder.py

class StringBuilder():

    def __init__(self) -> None:
        self.string = ""

    def add(self, string_to_add):
        self.string += string_to_add

    def size(self):
        return len(self.string)
    
    def output(self):
        return self.string

