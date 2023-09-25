# File: lib/todo_list.py

# challenge imports
from lib.todo import Todo


class TodoList:
    """Track tasks and mark complete or not"""

    def __init__(self):
        self._todo_list = []

    def add(self, todo):
        """Adds instance of todo class to task list attribute/property"""
        if not isinstance(todo, Todo):
            raise Exception("Invalid type - please add task as instance of todo")
        self._todo_list.append(todo)
      
    def incomplete(self):
        """Returns list of incomplete todos"""
        incomplete = [task for task in self._todo_list if task.complete == False]
        return incomplete

    def complete(self):
        """Returns list of compelte todos"""
        complete = [task for task in self._todo_list if task.complete == True]
        return complete

    def give_up(self):
        """Marks all to dos as complete"""
        if self.incomplete() == []:
            return "You have no tasks to complete"
        for task in self.incomplete():
            task.mark_complete()
