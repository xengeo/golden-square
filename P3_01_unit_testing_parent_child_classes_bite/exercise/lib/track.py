# File: lib/track.py

class Track:
    def __init__(self, title, artist):
        """Initialise private attributes"""
        self._title = title
        self._artist = artist

    def matches(self, keyword):
        """Searches for matches with keyword 
        Returns: False / True (for subset or superset match)"""
        return    keyword in self._title  \
               or keyword in self._artist \
               or self._title in keyword  \
               or self._artist in keyword