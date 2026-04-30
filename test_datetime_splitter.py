import pytest
from datetime_splitter import datetime_splitter

def test_same_day():
    assert datetime_splitter("2024-04-15 08:30:00","2024-04-15 16:30:00") == 1

def test_midnight():
    assert datetime_splitter("2024-04-15 08:30:00","2024-04-16 02:30:00") == 2

def test_multiple():
    assert datetime_splitter("2024-04-15 08:30:00","2024-04-20 02:30:00") == 6

def test_invalid_input():
    with pytest.raises(ValueError):
        datetime_splitter("######","#####")

def test_end_before_start():
    with pytest.raises(ValueError):
        datetime_splitter("2024-04-20 02:30:00","2024-04-15 08:30:00")


