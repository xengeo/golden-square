# File: P2_06_design_a_class/challenge/tests/test_music_library.py
from lib.music_library import MusicLibrary
import pytest

"""
Initially, there should be no tracks in the music library
# list_tracks should return a message "You have no saved tracks"
"""

def test_initially_no_tracks():
    my_music = MusicLibrary()
    result = my_music.list_tracks()
    assert result == "You have no saved tracks"


"""
Given one track add_track should add the track
# list_tracks should list the track
"""
def test_add_one_track_to_music_lib():
    my_music = MusicLibrary()
    my_music.add_track('Song 1')
    result = my_music.list_tracks()
    assert result == "You have listened to: Song 1"


"""
Given 3 tracks add_track should add the tracks
# list_tracks should list the tracks
"""
def test_add_three_tracks_to_music_lib():
    my_music = MusicLibrary()
    my_music.add_track('Song 1')
    my_music.add_track('Song 2')
    my_music.add_track('Song 3')
    result = my_music.list_tracks()
    assert result == "You have listened to: Song 1, Song 2, Song 3"


"""
Given empty string 
add_track should not add the track and raise error
# list_tracks should not list the song
"""
def test_add_empty_string_raises_error_and_list_tracks_empty():
    my_music = MusicLibrary()
    with pytest.raises(Exception) as e:
        my_music.add_track('')
    error_message = str(e.value)
    assert error_message == "Error: invalid track, please provide a track name"
    assert my_music.list_tracks() == "You have no saved tracks"


"""
Given an invalid input (not string)
add_track should not add the track and raise error
# list_tracks should not list the song
"""
def test_add_invalid_type_raises_error_and_list_tracks_empty():
    my_music = MusicLibrary()
    with pytest.raises(Exception) as e:
        my_music.add_track(4543)
    error_message = str(e.value)
    assert error_message == "Error: invalid track, please provide a track name"
    assert my_music.list_tracks() == "You have no saved tracks"