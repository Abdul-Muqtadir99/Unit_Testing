from lib.grattitudes import *

"""
Starts with empty list Which is
fromatted to string
"""

def test_grattitudes_initially_empty():
    grattitude = Gratitudes()
    assert grattitude.format() == "Be grateful for: "

"""
Test adding of multiple grattitudes
formats correctly
"""

def test_adding_multiple_grattitudes_formats_correctly():
    grattitude = Gratitudes()
    grattitude.add("Parents")
    grattitude.add("Life")
    grattitude.add("Everthing you have")
    assert grattitude.format() == "Be grateful for: Parents, Life, Everthing you have"