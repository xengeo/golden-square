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

                                                                      ┌──────────────────────┐
                                                                      │Contact()             │
                                                                      │                      │
┌───────────────────────────────────┐                                 │ attr. name           │
│Diary()                            │   ┌───────────────────────┐     │       number         │
│                                   │   │DiaryEntry()           │     │                      │
│ attr: entry_list                  │   │                       │     │                      │
│                                   │   │attr. title, contents  │     │                      │
│ add_entry()                       │   │     contact_list      │     │                      │
│                                   │   │     task_list         ├─────►                      │
│ list_all_entries()                │   │ format_entry()        │     └──────────────────────┘
│                                   ├───► count_words()         │
│ find_best_entry()                 │   │ reading_time()        │     ┌──────────────────────┐
│                                   │   │ set_task()            │     │Task()                │
│ find_phone_numbers()              │   │ list_task()           │     │                      │
│                                   │   │ set_contact()         │     │ attr. task           │
│                                   │   │ list_contact()        ├─────►       complete       │
│                                   │   │ find_number()         │     │                      │
│                                   │   │                       │     │  mark_complete()     │
│                                   │   └───────────────────────┘     │                      │
└───────────────────────────────────┘                                 │                      │
                                                                      │                      │
                                                                      │                      │
                                                                      └──────────────────────┘

```

_Also design the interface of each class in more detail._

```python

class Diary():

    def __init__(self):
        # Parameters: None
        # Side-effects: Initialises entry_list private property

    def add_diary_entry(self, entry):
        # Parameters: instance of a DiaryEntry class
        # Returns: None
        # Side-effects: Append instance of DiaryEntryy to entry_list
        pass

    def list_all_entries(self):
        # Parameters: None
        # Returns: List of all elements in entry_list
        pass

    def find_best_entry(self, wpm:int, minutes:int):
        # Parameters: wpm, minutes 
        # Returns: The diary entry object the user can read given wpm & minutes
        pass

    def find_phone_numbers(self):
        # Parameters: None
        # Returns: List of all mobile phone numbers found in diaryentries
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
        #       contact instance of contact class
        # Side effect:
        #       Adds contact to the contact list

    def add_task(self, task):
        # Parameters:
        #           task: Instance of task class
        # Side effect:
        #           Adds task to the task list

    def count_words(self):
        """Returns: An integer representing the number of words in the contents"""
        # Parameters: None
        # Returns: Number of words in contents of diary entry obj (int)
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
        # Parameters:   None
        # Returns:      List all contacts stored in entry
        pass

    def list_tasks(self):
        # Parameters:   None
        # Returns:      List all tasks stored in entry
        pass

    def find_phone_number(self):
        # Parameters: None
        # Returns: List of numbers found in entry
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
# """
# Test add method with 2 valid entires.
# All method returns list with added entries included.
# """
# diary = ()
# diary_entry1 = DiaryEntry('Title1', 'one two three')
# diary.add(diary_entry1)
# diary.all() # => [diary_entry1]


# """Test add method ignores invalid entries"""
# diary = ()
# diary_entry1 = 'Entry1'
# diary.add(diary_entry1)
# diary.all() # => []


# """Test find the best entry given two entires with
# 2 words length and 4 words length with 2wpm and 1min
# returns """
# diary = ()
# diary_entry1 = DiaryEntry('Title1', 'one two')
# diary_entry1 = DiaryEntry('Title2', 'three four five six')
# diary.add(diary_entry1)
# diary.add(diary_entry2)
# diary.find_the_best_entry(2, 1) #=> [entry1]

# """Given and 0minutes find the best entry returns an error"""
# diary = ()
# diary_entry1 = DiaryEntry('Title1', 'one two')
# diary_entry1 = DiaryEntry('Title2', 'three four five six')
# diary.add(diary_entry1)
# diary.add(diary_entry2)
# diary.find_the_best_entry(1, 0) #=> error("Minutes can't be 0")

# """Given and 0 wpm find the best entry returns an error"""
# diary = ()
# diary_entry1 = DiaryEntry('Title1', 'one two')
# diary_entry1 = DiaryEntry('Title2', 'three four five six')
# diary.add(diary_entry1)
# diary.add(diary_entry2)
# diary.find_the_best_entry(0, 1) #=> error("Wpm can't be 0")


```
### Diary Entry integration
``` python

# """Given a valid contact
# List method returns this contact in a list"""
# entry = DiaryEntry('Title1', 'one two')
# contact = Contact('name', '12345678')
# entry.set_contact(contact)
# entry.list_contacts() #=> [contact]

# """
# Given a task to DiaryEntry set_task
# list_task returns that task
# """
# entry_1 = DiaryEntry('Title1', 'one two')
# entry_1.set_task('Walk the dog')
# entry_1.list_task() # => ['Walk the dog']

# Other tests: test find_number()

```
###
## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

# DiaryEntry()
# ============
# """
# Given a title and contents,
# we see the titel and contents reflected in title and contents properties
# """
# entry_1 = DiaryEntry('Title1', 'one two')
# entry_1.title # => 'Title1'
# entry_1.contents # => 'one two'

# """
# Given a title and contents with 4 words,
# count_words() returns: int 4
# """
# entry_1 = DiaryEntry('Title1', 'one two three four')
# entry_1.count_words() # => 4

# """
# Given a title and contents with 4 words,
# wpm of 2
# reading_time() returns: 
# """
# entry_1 = DiaryEntry('Title1', 'one two three four')
# entry_1.reading_time(2) # => 2

# Contact()
# ============

# """
# Given a name and number
# name and number attributes return given values
# """
# contact_1 = Contact('Name1', '076452347851')
# contact_1.name # => 'Name1'
# contact_1.number # => '076452347851'

# Task()
# ============
# """
# Given a task
# task attribute return given task
# complete atteribute returns default False
# """
# tast_1 = Task('Walk the dog')
# tast_1.task # => 'Walk the dog'
# tast_1.complete # => False

# """
# Given a task
# task attribute return given task
# When we run mark_complete()
# complete atteribute returns default True
# """
# tast_1 = Task('Walk the dog')
# tast_1.task # => 'Walk the dog'
# tast_1.complete # => False
# task_1.mark_complete()
# tast_1.complete # => True



```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
