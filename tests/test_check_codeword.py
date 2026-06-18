from lib.check_codeword import *

"""
If the codeword is correct
Returns "correct, Come in."
"""

def test_correct_codeword_returns_corect():
    assert check_codeword("horse") == "Correct! Come in."


"""
If codeword is wrong, return WRONG!
"""

def test_incorrect_codeword():
     assert check_codeword("Wrong") == "WRONG!"

"""
if codeword has correct first and las letter close
"""

def test_close_codeword():
    assert check_codeword("house") == "Close, but nope."

"""
Test correct first letter, inccorect last leter
returns Wrong
"""

def test_correct_first_letter_only_codeword():
    assert check_codeword("hand") == "WRONG!"

"""
Test correct first letter, inccorect last leter
returns Wrong
"""

def test_correct_last_letter_only_codeword():
    assert check_codeword("spine") == "WRONG!"