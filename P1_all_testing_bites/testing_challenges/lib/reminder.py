# File: lib/reminder.py

class Reminder():
    
    def __init__(self, name) -> None:
        self.name = name

    def remind_me_to(self, task):
        self.task = task
    
    def remind(self):
        return f"{self.task}, {self.name}"