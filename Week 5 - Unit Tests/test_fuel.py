from fuel import convert
from fuel import gauge

def test_convert():
    assert convert("cat/dog") == "Error"
    assert convert("1/4") == 25

def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
