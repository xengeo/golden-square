# File: P2_06_design_a_class/challenge/lib/music_library.py

"""Class to track music"""

class MusicLibrary:

    def __init__(self):
        self._my_tracks = []

    def add_track(self, track:str):
        if track == '' or type(track) != str:
            raise Exception(
                "Error: invalid track, please provide a track name"
                )
        self._my_tracks.append(track)

    def list_tracks(self):
        if self._my_tracks:
            return f"You have listened to: {', '.join(self._my_tracks)}"
        return "You have no saved tracks"