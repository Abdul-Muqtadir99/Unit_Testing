import pytest
from lib.password_checker import *

"""
When we use a password exactly 8 characters
we should return true
"""
def test_eigh_character_password_length():
    password = PasswordChecker()
    result = password.check("password")
    assert result == True

"""
When we use a password longer than 8 characters
we should return true
"""
def test_long_correct_password_length():
    password = PasswordChecker()
    result = password.check("password12345")
    assert result == True

"""
When password is < 8 
We get an error message
"""

def test_incorrect_password_legnth():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check("pass")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."
    
"""
When we use a password exactly 7 characters
we should return true
"""
def test_seven_character_password_length():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check("1234567")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."