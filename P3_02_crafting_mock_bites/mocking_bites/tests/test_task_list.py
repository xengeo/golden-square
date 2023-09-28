# standard imports
from unittest.mock import Mock

# codebase imports
from lib.task_list import TaskList

"""
Test task list initially empty
"""
def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []

"""
Test all_complete list initially False
"""
def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False


# Unit test `#tasks` and `#all_complete` behaviour
"""
Given 1 mock task
task_list returns list with mock task
"""
def test_add_mock_task_returned_in_task_list():
    task_list = TaskList()
    mock_task_1 = Mock()
    task_list.add(mock_task_1)
    assert task_list.all() == [mock_task_1]


"""
Given 2 mock tasks
task_list returns list with both mock tasks
"""
def test_add_two_mock_task_returned_in_task_list():
    task_list = TaskList()
    mock_task_1 = Mock()
    task_list.add(mock_task_1)
    mock_task_2 = Mock()
    task_list.add(mock_task_2)
    assert task_list.all() == [mock_task_1, mock_task_2]

"""
Given 1 complete mock task, 1 incomplete mock task
#all_complete returns False
"""
def test_one_complete_one_incompelte_mock_all_complete_returns_false():
    
    task_list = TaskList()

    mock_task_1 = Mock()
    mock_task_2 = Mock()

    mock_task_1.is_complete.return_value = True
    mock_task_2.is_complete.return_value = False
    
    task_list.add(mock_task_1)
    task_list.add(mock_task_2)
    
    assert task_list.all_complete() == False

"""
Given 2 complete mock tasks,
#all_complete returns True
"""

def test_two_complete_mocks_all_complete_returns_true():
    
    task_list = TaskList()

    mock_task_1 = Mock()
    mock_task_2 = Mock()

    mock_task_1.is_complete.return_value = True
    mock_task_2.is_complete.return_value = True
    
    task_list.add(mock_task_1)
    task_list.add(mock_task_2)
    
    assert task_list.all_complete() == True