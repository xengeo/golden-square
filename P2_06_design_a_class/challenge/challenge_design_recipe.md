# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_
As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.
_

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class MusicLibrary:

    def __init__(self):
        # Parameters:
        #   Nothing
        # Side effects:
        #   Initialise an empty list to store songs in an instance variable
        pass # No code here yet

    def add_track(self, track:str):
        # Parameters:
        #   track: string representing a track the user has listened to
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the track to the track list
        pass # No code here yet

    def list_tracks(self):
        # Returns:
        #   Lists of track the user has listened to in a user friendly format
        # Side-effects:
        #   No side-effects
        pass # No code here yet

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

"""
Initially, there should be no tracks in the music library
# list_tracks should return a message "You have no saved tracks"
"""
my_music = MusicLibrary()
my_music.list_tracks() # => "You have no saved tracks"


"""
Given one track add_track should add the track
# list_tracks should list the track
"""
my_music = MusicLibrary()
my_music.add_track('Song 1')
my_music.list_tracks() # => "You have listened to: Song 1"


"""
Given 3 tracks add_track should add the tracks
# list_tracks should list the tracks
"""
my_music = MusicLibrary()
my_music.add_track('Song 1')
my_music.add_track('Song 2')
my_music.add_track('Song 3')
my_music.list_tracks() # => "You have listened to: Song 1, Song 2, Song 3"


"""
Given empty string 
add_track should not add the track and raise error
# list_tracks should not list the song
"""
my_music = MusicLibrary()
my_music.add_track('') # => raise error "Error: invalid track, please provide a track name"
my_music.list_tracks() # => "You have no saved tracks"


"""
Given an invalid input (not string)
add_track should not add the track and raise error
# list_tracks should not list the song
"""
my_music = MusicLibrary()
my_music.add_track(24235) # => raise error "Error: invalid track, please provide a track name"
my_music.list_tracks() # => "You have no saved tracks"

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->