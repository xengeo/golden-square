# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem
> As a user
So that I can record my experiences
I want to keep a regular diary

> As a user
So that I can reflect on my experiences
I want to read my past diary entries

> As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

> As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

> As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
Nouns:
    - diary
    - diary entries
    - tasks
    - todo list
    - contacts [mobile number]

Verbs:
    - record (add)
    - read (get) [entries]
    - select [entires]
    - track [contacts ]
    - list [contacts]


 ┌──────────────────────────────┐
 │Diary:                        │                                   ┌───────────────────────────────┐
 │                              │                                   │                               │
 │- Property: entry_list        │                                   │                               │
 │- add entries()               │                                   │                               │
 │- list all entries()          │                                   │                               │
 │- find best entry()           │                                   │                               │
 │                              │                                   │                               │
 │                              │                                   │                               │
 │                              │                                   │                               │
 │                              │                                   │                               │
 │                              │                                   │                               │
 │                              │                                   │                               │
 │                              │                                   │                               │
 └──────────────┬───────────────┘                                   │                               │
                │                                                   │                               │
                │                                                   └───────────────────────────────┘
                │  Diary stores list of entries
                │
                │
                │
                ▼
 ┌──────────────────────────────┐
 │Entry                         │                       ┌─────────────────────────────┐
 │                              │                       │ Contact                     │
 │Properties: title, contents,  │                       │ Properties: name, number    │
 │            contact_list,     │                       │                             │
 │            task_list         │Entry stores list of   │                             │
 │Methods:                      │contacts.              │                             │
 │Count_words()                 ├─────────────────────► │                             │
 │Add the contact()             │                       │                             │
 │List all the contacts()       │                       │                             │
 │                              │                       │                             │
 │                              │                       │                             │
 │                              │                       │                             │
 └───────────────┬──────────────┘                       └─────────────────────────────┘
                 │
                 │
                 │
                 │ Entry Stores                 Nouns:
                 │                                  - diary
                 │                                  - diary entries
                 │                                  - tasks
                 ▼                                  - todo list
   ┌────────────────────────────┐                   - contacts [mobile number]
   │                            │
   │TaskList:                   │               Verbs:
   │Properties: list_of_tasks   │                   - record (add)
   │                            │                   - read (get) [entries]
   │ Methods:                   │                   - select [entires]
   │Adds()                      │                   - track [contacts ]
   │Incomplete()                │                   - list [contacts]
   │Complete()                  │
   │Give_up()                   │
   │                            │
   │                            │
   │                            │
   └────────────┬───────────────┘
                │
                │
                │
                │
                │
                │
                ▼
┌───────────────────────────────┐
│                               │
│Task:                          │
│Properties: task, complete     │
│                               │
│                               │
│Methods:                       │
│Mark_complete()                │                                                            null
│                               │
│                               │
│                               │
│                               │
│                               │
└───────────────────────────────┘

```

_Also design the interface of each class in more detail._

```python

class Diary():

    def __init__(self):
        # entry_list property


    def add_diary_entry(self):
        # Add instance of diary entry to entry_list
        pass


    def list_all_entries(self):
        # List all entries
        pass

    def find_best_entry(self, wpm, minutes):
        pass


class DiaryEntry:

    def __init__(self, title:str, contents:str) -> None: 
    # self.title = title          # Public property
    # self.contents = contents    # Public property
    # self._contact_list = []
    # self._task_list = []
        pass

    def add_contact(self, contact):
        # Parameters:
            # contact instance of contact class
        # Side effect
        # Adds contact to the contact list

    def add_task(self, task):
        # Parameters:
            # task: Instance of task class
        # Side effect
        # Adds task to the task list

    def count_words(self):
    """Returns: An integer representing the number of words in the contents"""
        pass

    def reading_time(self, wpm):
    # Parameters:
    #   wpm: an integer representing the number of words the user can read
    #        per minute
    # Returns:
    #   An integer representing an estimate of the reading time in minutes
    #   for the contents at the given wpm.
        pass

    def list_contacts(self):
        # list all contacts
        pass

    def list_tasks(self):
        # list all task
        pass



class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        pass

    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        pass


class Contact:
    # Public Properties:
        #   name: string representin contact name
        #   number: string representing contact number
    def __init__(self, name, number):
    # Parameters:
    #   name: string representin contact name
    #   number: string representing contact number
    # Side-effects:
    # sets name and number properties
    pass

    def format():
        # Returns name and number in user friendly format
    
    pass

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

### Integration test
```python
"""
Test add method with 2 valid entires.
All method returns list with added entries included.
"""
diary = ()
diary_entry1 = DiaryEntry('Title1', 'one two three')
diary.add(diary_entry1)
diary.all() # => [diary_entry1]


"""Test add method ignores invalid entries"""
diary = ()
diary_entry1 = 'Entry1'
diary.add(diary_entry1)
diary.all() # => []


"""Test find the best entry given two entires with
2 words length and 4 words length with 2wpm and 1min
returns """
diary = ()
diary_entry1 = DiaryEntry('Title1', 'one two')
diary_entry1 = DiaryEntry('Title2', 'three four five six')
diary.add(diary_entry1)
diary.add(diary_entry2)
diary.find_the_best_entry(2, 1) #=> [entry1]

"""Given and 0minutes find the best entry returns an error"""
diary = ()
diary_entry1 = DiaryEntry('Title1', 'one two')
diary_entry1 = DiaryEntry('Title2', 'three four five six')
diary.add(diary_entry1)
diary.add(diary_entry2)
diary.find_the_best_entry(1, 0) #=> error("Minutes can't be 0")

"""Given and 0 wpm find the best entry returns an error"""
diary = ()
diary_entry1 = DiaryEntry('Title1', 'one two')
diary_entry1 = DiaryEntry('Title2', 'three four five six')
diary.add(diary_entry1)
diary.add(diary_entry2)
diary.find_the_best_entry(0, 1) #=> error("Wpm can't be 0")

```
### Diary Entry integration
``` python

"""Given a valid contact
List method returns this contact in a list"""
entry = DiaryEntry('Title1', 'one two')
contact = Contact('name', '12345678')
entry.add_contact(contact)
entry.list_contacts() #=> [contact]

```
###
## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given a track with a title and an artist
We see the title reflected in the title property
"""
track = Track("Carte Blanche", "Veracocha")
track.title # => "Carte Blanche"
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
