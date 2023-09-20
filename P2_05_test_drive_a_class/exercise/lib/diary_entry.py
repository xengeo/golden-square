# File: P2_05_test_drive_a_class/lib/diary_entry.py
import math


class DiaryEntry:
    def __init__(self, title:str, contents:str):
        # Parameters:
        #   title: string
        #   contents: string
        if title == '' or contents == '':
            raise Exception("Diary entries must have a title and contents")
        self._title = title
        self._contents = contents
        self._read_so_far = 0


    def format(self):
        "format diary entry into summary"
        return f'{self._title}: {self._contents}'


    def count_words(self):
        "counts words in diary entry"
        words = self.format().split()
        return len(words)


    def reading_time(self, wpm:int):
        "returns reading time in minutes for given reading speed (wpm:int)"
        if wpm == 0:
            raise Exception('Cannot calculate reading time with wpm of 0')
        contents_word_count = len(self._contents.split())
        reading_time = contents_word_count / wpm
        return math.ceil(reading_time)


    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        
        num_words_user_can_read = wpm * minutes

        words = self._contents.split()
        if self._read_so_far >= len(words):
            self._read_so_far = 0

        chunk_start = self._read_so_far
        chunk_end = self._read_so_far + num_words_user_can_read

        chunk_words = words[chunk_start:chunk_end]

        self._read_so_far = chunk_end

        return ' '.join(chunk_words)
        