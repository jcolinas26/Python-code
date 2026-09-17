from plates import is_valid

def test_plate_lon():
    assert is_valid("A") == False
    assert is_valid("AAA22222") == False
    assert is_valid("CS50") == True

def test_start_letter():
    assert is_valid("1") == False
    assert is_valid("A1A222") == False
    assert is_valid("CS50") == True

def test_no_punctuation():
    assert is_valid("HELLO, WORLD") == False
    assert is_valid("CS,50") == False
    assert is_valid("CS50") == True

def test_numbers_at_end():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True

#valid: CS50
#invalid: CS05