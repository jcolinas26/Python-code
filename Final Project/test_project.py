from project import format_price

def test_parse_change():
    assert format_price(64635.919) == "$64,635.92"
    assert format_price(0.5) == "$0.50"
    assert format_price(1000) == "$1,000.00"