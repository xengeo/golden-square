# File: challenge/tests/test_todo_list_unit,py

# standard imports
import pytest

# challenge imports
from lib.todo_list import TodoList


"""
This file contains unit tests for the class TodoList
"""

"""
Test instantiation of TodoList class
"""
def test_instantiate_todo_list_class():
    task_list = TodoList() 


"""
Add task
Test with no complete tasks
#complete returns empty task list []
"""
def test_no_tasks_complete_returns_empty_list():
    task_list = TodoList() 
    assert task_list.complete() == []
    assert task_list.incomplete() == []


"""
Test give_up when task_list empty
"""
def test_give_up_when__task_list_empty():
    task_list = TodoList() 
    assert task_list.give_up() == "You have no tasks to complete"



"""
Test add one non todo instance to todo list
# incomplete returns the list with task
"""
def test_non_todo_instance_to_todo_list_returns_error():
    todo_list = TodoList()
    with pytest.raises(Exception) as err:
        todo_list.add(['first_task'])
    error_message = str(err.value)
    assert error_message == "Invalid type - please add task as instance of todo"