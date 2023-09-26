# File: lib/diary_entry.py

import math

class DiaryEntry:
    """Class for a single diary entry"""

    def __init__(self, title:str, contents:str) -> None: 
        """initialise attributes"""

        self.title = title          # Public property
        self.contents = contents    # Public property
        self._contact_list = []
        self._task_list = []


    def count_words(self):
        """Returns: An integer representing the number of words in the contents"""
        return len(self.contents.split())


    def reading_time(self, wpm:int):
        """wpm = no. of words user can read per min. Returns: int, reading time estimate in mins"""

        if wpm == 0:
            raise Exception('wpm cannot be 0')
        
        words = self.count_words()
        reading_time = words / wpm  # Minutes to read all words

        return math.ceil(reading_time)


    def add_contact(self, contact):
        # Parameters:
        #       contact instance of contact class
        # Side effect:
        #       Adds contact to the contact list
        self._contact_list.append(contact)


    def list_contacts(self):
        # Parameters:   None
        # Returns:      List all contacts stored in entry
        return self._contact_list
    

    def add_task(self, task):
        # Parameters:
        #           task: Instance of task class
        # Side effect:
        #           Adds task to the task list
        self._task_list.append(task)


    def list_tasks(self):
        # Parameters:   None
        # Returns:      List all tasks stored in entry
        return self._task_list



        