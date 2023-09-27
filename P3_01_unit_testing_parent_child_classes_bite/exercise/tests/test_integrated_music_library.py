# File: tests/test_integrated_music_library.py

from lib.music_library import MusicLibrary
from lib.track import Track


"""
Test add a track the MusicLibrary using #add
#track_list returns instance of track
"""
def test_add_track_returns_track_in_track_list():
    my_library = MusicLibrary()
    track_1 = Track('Title1', 'Artist1')
    my_library.add(track_1)
    assert my_library.track_list == [track_1]


"""
Given keyword exact match for title 
#search returns: List with track
"""
def test_title_exact_match_search_returns_list_with_track():
    my_library = MusicLibrary()
    track_1 = Track('Title1', 'Artist1')
    my_library.add(track_1)
    assert my_library.search('Title1') == [track_1]

"""
Given keyword exact match for artist 
#search returns: List with track
"""
def test_artist_exact_match_search_returns_list_with_track():
    my_library = MusicLibrary()
    track_1 = Track('Title1', 'Artist1')
    my_library.add(track_1)
    assert my_library.search('Artist1') == [track_1]


"""
Given keyword no match for artist or title
#search returns: []
"""
def test_matched_search_returns_list_with_track():
    my_library = MusicLibrary()
    track_1 = Track('Title1', 'Artist1')
    my_library.add(track_1)
    assert my_library.search('no match') == []


"""
Given title subset of keyword 
#search returns: True
"""
def test_title_subset_matched_search_returns_list_with_track():
    my_library = MusicLibrary()
    track_1 = Track('Title1', 'Artist1')
    my_library.add(track_1)
    assert my_library.search('Title176756') == [track_1]


"""
Given artist subset of keyword 
#search returns: True
"""
def test_artist_subset_matched_search_returns_list_with_track():
    my_library = MusicLibrary()
    track_1 = Track('Title1', 'Artist1')
    my_library.add(track_1)
    assert my_library.search('Artist176756') == [track_1]


"""
Test search for keyword when no tracks are added
Returns: "No tracks to search"
"""
def test_search_with_no_tracks_stored_returns_message():
    my_library = MusicLibrary()
    assert my_library.search('no match') == []