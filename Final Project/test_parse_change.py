from project import parse_change

def test_parse_change():
    assert parse_change(-0.408) == "▼ 0.41% (down)"
    assert parse_change(0.408) == "▲ 0.41% (up)"
    assert parse_change(0) == "▲ 0.00% (up)"