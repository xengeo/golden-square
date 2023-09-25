# File: challenege/tests/test_todo_list.py

# standard imports
import pytest 

# my imports
from lib.todo_list import TodoList
from lib.todo import Todo


"""
Test add one incomplete task to do list
# incomplete returns the list with task
"""
def test_incomplete_returns_task_after_adding_task():
    todo_list = TodoList()
    first_task = Todo(task="First Task")
    todo_list.add(first_task)
    assert todo_list.incomplete() == [first_task]



"""
Add 3 tasks
Mark 1 as complete
Return all complete tasks [task2]
Return all incomplete tasks [task1, task3]
"""
def test_tasks_completed_returned_in_list():
    todo_list = TodoList()
    first_task = Todo("First Task")
    second_task = Todo("Second Task")
    third_task = Todo("Third Task")
    todo_list.add(first_task)
    todo_list.add(second_task)
    todo_list.add(third_task)
    second_task.mark_complete()
    assert todo_list.complete() == [second_task]
    assert todo_list.incomplete() == [first_task, third_task]


"""
Add tasks
Mark some as complete
Test give up on all task
#complete returns list of all tasks 
"""
def test_give_up_complete_returns_all_tasks():
    todo_list = TodoList()
    first_task = Todo("First Task")
    second_task = Todo("Second Task")
    third_task = Todo("Third Task")
    todo_list.add(first_task)
    todo_list.add(second_task)
    todo_list.add(third_task)
    todo_list.give_up()
    assert todo_list.complete() == [first_task, second_task, third_task]
    assert todo_list.incomplete() == []


