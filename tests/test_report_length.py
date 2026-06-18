from lib.report_length import *

def test_report_length_longer_string():
    result = report_length("hello")
    assert result == "This string was 5 characters long."

def test_report_length_shorter_string():
    result = report_length("me")
    assert result == "This string was 2 characters long."