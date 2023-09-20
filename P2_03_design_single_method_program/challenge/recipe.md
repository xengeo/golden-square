# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO._

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def includes_todo(text:str):
    """Checks text for '#TODO'

    Parameters: 
        text: a string containing words

    Returns: 
        Confirms whether text includes '#TODO' with a string.
        Returns: This text includes a #TODO.
        or
        Returns: This text does not include a #TODO.
        
    
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
Given a string containing only "#TODO"
Returns: "This text includes a #TODO."
"""
includes_todo('#TODO') => "This text includes a #TODO."



"""
Given an empty string
Returns: "This text does not include a #TODO."
"""
includes_todo('') => "This text does not include a #TODO."


"""
Given a long text with #TODO in it
Returns: "This text includes a #TODO."
"""
includes_todo() => "This text includes a #TODO."


"""
Given a long text without #TODO in it
Returns: "This text does not include a #TODO."
"""
includes_todo() => "This text does not include a #TODO."


"""
Given the wrong data type
Returns: "Error: wrong data type submitted, please input text/strings only."
"""
includes_todo(123456) => "Error: wrong data type submitted, please input text/strings only."


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