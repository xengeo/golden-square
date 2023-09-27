# File: lib/music_library.py


class MusicLibrary:
    """
    Music Library to store Track instances.\n
    Attributes: self.track_list
    Methods: add() search()
    """

    def __init__(self):
        self.track_list = []

    def add(self, track):
        """
        Adds instance of Track to self.track_list
        Returns: Nothing
        """
        self.track_list.append(track)

    def search(self, keyword):
        """
        Searches track title and artist for keyword
        Returns: List of matched Track instances
        """
        return [
            track for track in self.track_list 
            if track.matches(keyword)
        ]