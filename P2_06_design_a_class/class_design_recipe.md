# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_
As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.
_

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class Tasks:

    def __init__(self):
        # Parameters:
        #   Nothing
        # Side effects:
        #   Initialise an empty list to store tasks in an instance variable
        pass # No code here yet

    def add_task(self, task:str):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the task list
        pass # No code here yet

    def list_tasks(self):
        # Returns:
        #   Lists task in a user friendly format
        # Side-effects:
        #   No side-effects
        pass # No code here yet

    def mark_complete(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Friendly message saying task is complete
        # Side-effects:
        #   Removes the task from the list
        pass
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a number as an input to add_task method
Raises an error
"""
task = Tasks()
task.add_task(234) # => "Input is invalid"

"""
Given an empty string as an input
Raises an error
"""
task = Tasks()
task.add_task('') # => "Input is invalid"

"""
Given a valid task as an input
Returns task list has our task inside
"""
task = Tasks()
task.add_task('First task')
task._task_list() # => ['First task']

"""
Given two tasks with the same content, it is not added to the list
Return that the task already exists
"""
task = Tasks()
task.add_task('First task')
task.add_task('First task')
task.list_tasks() # => ['First task']

"""
Given three different tasks 
list_task methods returns the three tasks
"""
task = Tasks()
task.add_task('First task')
task.add_task('Second task')
task.add_task('Third task')
task.list_tasks() # => ['First task', 'Second task', 'Third task']

"""
Running list_tasks without having add any task
Returns: User friendly message
"""
task = Tasks()
tasks.list_tasks() # => "You have no tasks to complete"

"""
Given a valid task as an input
#mark_complete removes the task from the task list
Returns: "taskname completed"
"""
task = Tasks()
task.mark_complete('Fifth task') # => "taskname completed"
task.list_tasks() # => "You have no tasks to complete"

"""
Given a invalid task as an input
#mark_complete raises an error "Input is invalid"
"""
task = Tasks()
task.mark_complete(12214) # => "Input is invalid"

"""
Given a task that is not in task_list as an input
#mark_complete returns a message "Task is not in the task list"
"""
task = Tasks()
task.mark_complete('task') # => "Task is not in the task list"


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