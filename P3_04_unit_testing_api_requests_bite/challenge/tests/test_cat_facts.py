
# standard imports
from unittest.mock import Mock

# codebase imports
from lib.cat_facts import CatFacts


"""
Test a fact is provided (using a requests mock)
"""
def test_fact_is_returned():

    requester_mock = Mock(name="requester")
    response_mock = Mock(name="response")

    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {
        "fact":"Cats have the largest eyes of any mammal.",
        "length":41
        }

    cat_facts = CatFacts(requester_mock)
    assert cat_facts.provide() == "Cat fact: Cats have the largest eyes of any mammal."
    