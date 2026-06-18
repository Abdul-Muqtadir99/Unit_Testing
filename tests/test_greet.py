from lib.greet import *

def test_greets_person_of_given_name():
    assert greet("Jon") == "Hello, Jon!"