# File: test/test_task_unit.py

from lib.task import Task

"""
Given a task
task attribute return given task
complete atteribute returns default False
"""
def test_task_assigned_correctly():
    task_1 = Task('Walk the dog')
    assert task_1.task == 'Walk the dog'
    assert task_1.complete == False

"""
Given a task
task attribute return given task
When we run mark_complete()
complete atteribute returns default True
"""
def test_mark_complete():
    task_1 = Task('Walk the dog')
    task_1.task # => 'Walk the dog'
    assert task_1.complete == False
    task_1.mark_complete()
    assert task_1.complete == True