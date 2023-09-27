# File: lib/track.py

class Track:
    def __init__(self, title, artist):
        # title and artist are both strings
        self._title = title
        self._artist = artist

    def matches(self, keyword):
        # keyword is a string
        # Returns true if the keyword matches either the title or artist
        return keyword in self._title or keyword in self._artist