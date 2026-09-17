from twttr import shorten

def test_argument():
    assert shorten("Hello") == "Hll"
    assert shorten("Hello World") == "Hll Wrld"
    assert shorten("Jorge") == "Jrg"