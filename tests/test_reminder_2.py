#
import pytest # <-- New code
from lib.reminder_2 import *


def test_reminder():
    reminder = Reminder("Kay")
    with pytest.raises(Exception) as e: ### <-- New code ###
        reminder.remind()
    error_message = str(e.value) ### <-- New code ###
    assert error_message == "No reminder set!"
