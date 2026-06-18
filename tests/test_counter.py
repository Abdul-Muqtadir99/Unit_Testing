from lib.counter import *

def test_counter_reports_total_after_adding_number():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 5 so far."
    counter.add(10)
    result = counter.report()
    assert result == "Counted to 15 so far."
    counter.add(-1)
    result = counter.report()
    assert result == "Counted to 14 so far."

# it is better to separate these into individual tests
# because each test checks one clear behaviour, so if
# one fails, it is easier to see exactly what part of
# the counter is broken.