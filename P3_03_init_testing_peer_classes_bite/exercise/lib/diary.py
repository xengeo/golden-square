# File: lib/diary.py

class Diary:
    def __init__(self, contents):
        if isinstance(contents, str):
            self._contents = contents
        else:
            raise Exception("Error: contents must be a string")

    def read(self):
        return self._contents
