from project import convert
from project import most_watched
from project import percentile

import pytest


def test_convert_1():
    assert convert("3OC2aPCuzjo")  == ('Electric Guest - Troubleman', '\nDownload Electric Guest\'s debut album "Mondo" : http://smarturl.it/mondo\n\nLike Electric Guest on Facebook : http://www.fa[...]

def test_convert_2():
    with pytest.raises(ValueError):
        convert("cat")

def test_convert_non_existing_id():
    with pytest.raises(ValueError):
        convert("3OC2aPCuzjk")

def test_most_watched_1():
    assert most_watched(0)  == ("IzfJfkqfgHM", 57)

def test_most_watched_2():
    with pytest.raises(TypeError):
        most_watched("0")

# Video with most views
def test_percentile_1():
    assert percentile("IzfJfkqfgHM")  == 100

# Video with 0 views
def test_percentile_2():
    assert percentile("iITHVFHTa6Q")  == 0

# Video with 4 views
def test_percentile_3():
    assert percentile("I4i1KcqWikY")  == 98.54
