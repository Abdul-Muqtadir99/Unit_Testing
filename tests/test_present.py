import pytest
from lib.present import *

""" 
When we try to wrap a wrapped present
We get an error message
"""

def test_wrap_throws_error_if_none():
    present = Present()
    present.wrap("Ps5")
    with pytest.raises(Exception) as e:
        present.wrap("ps5")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

"""
When we unrap without wrapping
we get an error message
"""
def test_unwrap_throws_error_if_none():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

"""
When we unrap contents that is wrapped
We get contents back
"""

def test_unwrap_returns_contents():
    present = Present()
    present.wrap("XBox")
    result = present.unwrap()
    assert result == "XBox"