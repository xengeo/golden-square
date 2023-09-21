import pytest
from lib.tasks import Tasks


"""
Given a number as an input to add_task method
Raises an error
"""
def test_add_tasks_with_invalid_input():
    task = Tasks()
    with pytest.raises(Exception) as e:
        task.add_task(234)
    error_message = str(e.value)
    assert error_message == "Input must be a string"


"""
Given an empty string as an input
Raises an error
"""
def test_add_task_with_empty_task():
    task = Tasks()
    with pytest.raises(Exception) as e:
        task.add_task('')
    error_message = str(e.value)
    assert error_message == "Input must be a string"


"""
Given a valid task as an input
Returns task list has our task inside
"""
def test_add_task_with_valid_input():
    task = Tasks()
    task.add_task('First task')
    assert task._task_list == ['First task']


"""
Given two tasks with the same content, it is not added to the list
Return that the task already exists
"""
def test_add_tasks_with_two_identical_tasks():
    task = Tasks()
    task.add_task('First task')
    assert task.add_task('First task') == "Task already exists"
    

"""
Given three different tasks 
list_task methods returns the three tasks
"""
def test_list_tasks_with_three_different_tasks():
    task = Tasks()
    task.add_task('First task')
    task.add_task('Second task')
    task.add_task('Third task')
    assert task.list_tasks() == ['First task', 'Second task', 'Third task']


"""
Running list_tasks without having add any task
Returns: User friendly message
"""
def test_list_task_with_empty_task_list():
    task = Tasks()
    assert task.list_tasks() == "Your list is empty"


"""
Given a valid task as an input
#mark_complete removes the task from the task list
Returns: "taskname completed"
"""
def test_mark_complete_with_valid_task():
    task = Tasks()
    task.add_task('First task')
    assert task.mark_complete('First task') == "First task completed"
    assert task.list_tasks() == "Your list is empty"

"""
Given a invalid task as an input
#mark_complete raises an error "Input is invalid"
"""
def test_mark_complete_with_invalid_input():
    task = Tasks()
    with pytest.raises(Exception) as e:
        task.mark_complete(654234235)
    error_message = str(e.value)
    assert error_message == "Input is invalid"


"""
Given a empty string task as an input
#mark_complete raises an error "Input is invalid"
"""
def test_mark_complete_with_invalid_input():
    task = Tasks()
    with pytest.raises(Exception) as e:
        task.mark_complete('')
    error_message = str(e.value)
    assert error_message == "Input is invalid"


"""
Given a task that is not in task_list as an input
#mark_complete returns a message "Task is not in the task list"
"""
def test_mark_complete_with_task_not_in_list():
    task = Tasks()
    task.add_task('First task')
    assert task.mark_complete('Second task') == "Task is not in the task list"