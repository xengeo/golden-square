# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute._

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def estimate_reading_time(text:str):
    """Estimates reading time for a text (200 words = 1 min)

    Parameters: 
        text: a string containing words

    Returns: 
        A sentence with an estimate of time in minutes.
        e.g. "This text will take XX mins to read."
    
    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects   
    """
    pass
```


## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a string of 200 words
Returns: "This text will take 1 mins to read"
"""
estimate_reading_time(text) => "This text will take 1 mins to read"

"""
Given a string of 300 words
Returns: "This text will take 1.5 mins to read"
"""
estimate_reading_time(text) => "This text will take 1.5 mins to read"

"""
Given a string of 400 words
Returns: "This text will take 2 mins to read"
"""
estimate_reading_time(text) => "This text will take 2 mins to read"

"""
Given an empty string
Returns: "Cannot give estimate of reading time if no text is given."
"""
estimate_reading_time('') => "Cannot give estimate of reading time if no text is given."

"""
Given a 5 word string
Returns: "This text will take 0.025 mins to read"
"""
estimate_reading_time('one two three four five') => "This text will take 0.025 mins to read"

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

```

Ensure all test function names are unique, otherwise pytest will ignore them!


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->