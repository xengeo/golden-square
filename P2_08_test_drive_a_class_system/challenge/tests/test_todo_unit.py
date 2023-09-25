# File: challenge/tests/test_todo_unit,py

# standard imports
import pytest

# challenge imports
from lib.todo import Todo


"""
This file contains unit tests for the class Todo
"""

"""
Test add a new task using Todo class
first_task.task returns task name
first_task.complete returns False
"""
def test_add_task_usingtodo():
    first_task = Todo('First Task')
    assert first_task.task == 'First Task'
    assert first_task.complete == False


"""
Test add empty task
raises error
"""
def test_empty_task_adding_raises_error():
    with pytest.raises(Exception) as err:
        first_task = Todo(task="")
    error_message = str(err.value)
    assert error_message == "Cannot add empty task"


"""
Test add single space task
raises error
"""
def test_single_space_char_task_adding_raises_error():
    with pytest.raises(Exception) as err:
        first_task = Todo(task=" ")
    error_message = str(err.value)
    assert error_message == "Cannot add empty task"


"""
Test add task of wrong type
raises error
"""
def test_wrong_task_type_adding_raises_error():
    with pytest.raises(Exception) as err:
        first_task = Todo(task=432)
    error_message = str(err.value)
    assert error_message == "Invalid type - task must be a string"


"""
Test marking a task as complete 
self.complete returns True
"""
def test_mark_task_as_complete():
    first_task = Todo('First Task')
    first_task.mark_complete()
    assert first_task.complete == True


"""Test mark complete a task that is already compeletes"""
def test_mark_complete_a_task_that_is_already_complete():
    first_task = Todo('First Task')
    first_task.mark_complete()
    assert first_task.mark_complete() == "This task is already complete"

