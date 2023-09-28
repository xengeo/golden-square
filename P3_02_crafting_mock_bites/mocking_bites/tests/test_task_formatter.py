# File: tests/test_task_formatter.py

# UNIT TESTS TaskFormatter()

from unittest.mock import Mock
from lib.task_formatter import TaskFormatter


"""
Format a task that is incomplete
"""
def test_format_an_incomplete_task():
    task = Mock()
    formatter = TaskFormatter(task)
    
    task.title = "Walk the dog"
    task.is_complete.return_value = False

    assert formatter.format() == "- [] Walk the dog"
    task.is_complete.assert_called()


"""
Format a task that is complete
"""
def test_format_a_complete_task():
    task = Mock()
    formatter = TaskFormatter(task)

    task.title = "Walk the dog"
    task.is_complete.return_value = True

    assert formatter.format() == "- [x] Walk the dog"
    task.is_complete.assert_called()
