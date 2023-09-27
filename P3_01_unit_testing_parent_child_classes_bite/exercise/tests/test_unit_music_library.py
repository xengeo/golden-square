# File: tests/test_unit_music_library.py
from unittest.mock import Mock
import pytest

from lib.music_library import MusicLibrary

"""
Tests initially music library tracks list is empty
"""
def test_initial_empty_track_list():
    my_library = MusicLibrary()
    assert my_library.track_list == []


"""
Tests add mock track first_track
#self.track_list returns list including track
"""
def test_add_mock_first_track_returns_track_list():
    my_library = MusicLibrary()
    first_track = Mock()
    my_library.add(first_track)
    assert my_library.track_list == [first_track]


"""
Tests add 2 mock tracks first_track, second_track
#self.track_list returns list including tracks
"""
def test_add_mock_two_tracks_returns_track_list():
    my_library = MusicLibrary()
    first_track = Mock()
    second_track = Mock()
    my_library.add(first_track)
    my_library.add(second_track)
    assert my_library.track_list == [first_track, second_track]


"""
Given a track, keyword matched
#search returns a list of matched track instance
"""
def test_search_returns_matched_track():
    my_library = MusicLibrary()
    first_track = Mock()
    first_track.matches.return_value = True
    my_library.add(first_track)
    assert my_library.search('keyword') == [first_track]


"""
Given a track, keyword unmatched
#search returns the empty list
"""
def test_search_returns_no_matches():
    my_library = MusicLibrary()
    first_track = Mock()
    first_track.matches.return_value = False
    my_library.add(first_track)
    assert my_library.search('keyword') == []