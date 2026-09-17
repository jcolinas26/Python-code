from bank import value

def test_value():
    assert value("Hello") == 0
    assert value("Hell") == 20
    assert value("Jorge") == 100