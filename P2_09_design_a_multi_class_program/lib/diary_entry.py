# File: lib/diary_entry.py

import math

class DiaryEntry:

    def __init__(self, title:str, contents:str) -> None: 
        self.title = title          # Public property
        self.contents = contents    # Public property
        self._contact_list = []
        self._task_list = []

    def count_words(self):
        """Returns: An integer representing the number of words in the contents"""
        return len(self.contents.split())

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        if wpm == 0:
            raise Exception('Cannot calculate reading time with wpm of 0')
        reading_time = 0
        words = self.count_words()
        reading_time += words / wpm  # Minutes to read all words
        return math.ceil(reading_time)


        