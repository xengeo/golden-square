# File: lib/diary.py
import math

class Diary:
    def __init__(self):
        self._diary_entries = []

    def add(self, entry) -> None:
        """        
        Parameters: entry: an instance of DiaryEntry
        Returns:    Nothing
        Side-effects:   Adds the entry to the entries list
        """

        self._diary_entries.append(entry)

    def all(self) -> list:
        """Returns: A list of instances of DiaryEntry"""
        return self._diary_entries

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        total_words = 0
        for entry in self._diary_entries:
            total_words += entry.count_words() 
        return total_words
        

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        total_reading_time = 0
        for entry in self._diary_entries:
            total_reading_time += entry.reading_time(wpm) 

        return f"{total_reading_time} minutes"

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.

        for entry in self._diary_entries:
            if entry.reading_time(wpm) <= minutes:
                return entry
            


# File: lib/diary_entry.py

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
        pass