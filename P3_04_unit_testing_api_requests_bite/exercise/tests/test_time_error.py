# File: tests/test_time_error.py

# To make this testable, you will need to create a mock for requests and 
# also deal with the behaviour of time.time() which is also non-deterministic.


# python standard imports
from unittest.mock import Mock

# codebase imports
from lib.time_error import TimeError


"""
Test getting time with mocks
"""
def test_return_time_diff_with_mocks():
    
    requester_mock = Mock(name="requester") # make a mock for requests lib
    response_mock = Mock(name="response") # make a mock for response object
    timer_mock = Mock(name="timer") # make a mock for time module

    requester_mock.get.return_value = response_mock # requester_mock get method returns the response_mock
    response_mock.json.return_value = {'unixtime': 20}
    timer_mock.time.return_value = 5

    time_error = TimeError(requester=requester_mock,
                           timer=timer_mock)

    result = time_error.error()
    assert result == 15