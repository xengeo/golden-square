# File: tests/test_unit_music_library.py

from lib.track import Track


"""
Test initialise a track
#matches returns True for title match only
"""
def test_one_track_keyword_match_title_returns_true():
    track_1 = Track('track_1', 'artist_1')
    assert track_1.matches('track_1') == True


"""
Test initialise a track
#matches returns True for artist match only
"""
def test_one_track_keyword_match_artist_returns_true():
    track_1 = Track('track_1', 'artist_1')
    assert track_1.matches('artist_1') == True


"""
Test initialise a track
#matches returns False for no match
"""
def test_one_track_keyword_unmatched_returns_False():
    track_1 = Track('track_1', 'artist_1')
    assert track_1.matches('jelly') == False