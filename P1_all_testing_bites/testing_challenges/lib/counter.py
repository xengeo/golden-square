# File: lib/counter.py

class Counter():

    def __init__(self) -> None:
        self.count = 0

    def add(self, num:int):
        self.count += num

    def report(self):
        return f"Counted to {self.count} so far."
    
    