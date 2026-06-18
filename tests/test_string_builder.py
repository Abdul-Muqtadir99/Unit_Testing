from lib.string_builder import  *

"""
Starts with empty string
length is zero
"""
def test_string_builder_returns_empty_string():
    builder = StringBuilder()
    assert builder.output() == ""
    assert builder.size() == 0

# The test below has been commented out becasue it
# is not needed. if the test for adding multiple strings
# further below, then this should work so has been made
#redundant (its testing the same thing.)

# """
# Adds one string and reports its size and output.
# """

# def test_adds_one_string_and_updates_size_and_output():
#     builder = StringBuilder()
#     builder.add("Hello")

#     assert builder.size() == 5
#     assert builder.output() == "Hello"

"""
Test adding multiple string counts the  concatanated string 
and returns the strings cocatanated
"""
#Better to seperate the below into two seperate tests,
#due for ease of debugging if one of the two assertions fail
def test_adds_multiple_strings_and_updates_size_and_output():
    builder = StringBuilder()
    builder.add("Hello")
    builder.add(" everyone!")
    assert builder.size() == 15
    assert builder.output() == "Hello everyone!"

