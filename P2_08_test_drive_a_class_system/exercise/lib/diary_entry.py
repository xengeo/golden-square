# File: lib/diary_entry.py

import math

class DiaryEntry:

    def __init__(self, title:str, contents:str) -> None: 
        self.title = title          # Public property
        self.contents = contents    # Public property
        self._read_so_far = 0

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

    def reading_chunk(self, wpm, minutes):
        """
        Returns:
            string: chunks of words that user can read in given wpm and minutes

        If rerun, returns to next chunk in diary content 
        and so on until it reaches the end
        """
        # words user can read in time given
        num_words_user_can_read = wpm * minutes

        words = self.contents.split() # get all words
        if self._read_so_far >= len(words):
            self._read_so_far = 0 # resets num of words read_so_far

        chunk_start = self._read_so_far # define start of word chunk
        chunk_end = self._read_so_far + num_words_user_can_read # define end of word chunk
        chunk_words = words[chunk_start:chunk_end] # get chunk of words bases on start and end point

        self._read_so_far = chunk_end

        return ' '.join(chunk_words)
        