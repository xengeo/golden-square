# File: lib/task_formatter.py

class TaskFormatter:
    def __init__(self, task): # task is an instance of Task
        self._task = task

    def format(self):
        # Returns the task formatted as a string.
        # If the task is not complete, the format is:
        # - [ ] Task title
        # If the task is complete, the format is:
        # - [x] Task title
        if self._task.is_complete():
            return f"- [x] {self._task.title}"
        else:
            return f"- [] {self._task.title}"
