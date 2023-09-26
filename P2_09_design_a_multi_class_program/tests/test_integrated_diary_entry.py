# File: tests/test_integrated_diary_entry.py

from lib.diary_entry import DiaryEntry
from lib.contact import Contact

"""Given a valid contact
List method returns this contact in a list"""
def test_set_contact_with_name_and_number_list_returns_list():
    entry = DiaryEntry('Title1', 'one two')
    contact = Contact('name1', '076452347851')
    entry.add_contact(contact)
    assert entry.list_contacts() == [contact]


"""
Given a task to DiaryEntry set_task
list_task returns that task
"""
def test_add_task_to_task_list():
    entry_1 = DiaryEntry('Title1', 'one two')
    entry_1.add_task('Walk the dog')
    assert entry_1.list_tasks() == ['Walk the dog']

# add more tests for invalid types