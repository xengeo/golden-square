# File: lib/todo.py

class Todo:
    """add single task and mark complete (False) or incomplete (True)"""

    def __init__(self, task):
        """Instantiate a task, complete status defaults to False"""
        if task == "" or task == " ":
            raise Exception("Cannot add empty task")
        elif type(task) != str:
            raise Exception("Invalid type - task must be a string")
        self.task = task    # public property
        self.complete = False   # public property

    def mark_complete(self):
        """Sets complete status to True"""
        if self.complete == True:
            return "This task is already complete"
        self.complete = True