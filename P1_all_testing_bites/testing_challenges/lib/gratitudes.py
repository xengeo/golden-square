# File: lib.gratitudes.py

class Gratitudes():
    def __init__(self) -> None:
        self.gratitudes = []

    def add(self, gratitude:str):
        self.gratitudes.append(gratitude)

    def format(self):
        formatted = "Be grateful for: "
        formatted += ', '.join(self.gratitudes)
        return formatted