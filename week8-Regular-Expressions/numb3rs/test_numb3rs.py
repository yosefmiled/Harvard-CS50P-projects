from numb3rs import validate

def test_single():
    assert validate("1.3.5.7") == True
    assert validate("1.0.5.0") == True

def test_words():
    assert validate("yes") == False
    assert validate("true") == False

def test_zeros():
    assert validate("00.001.34.56") == False
    assert validate("90.80.0.20") == True

def test_triple():
    assert validate("000.09.90.4") == False
    assert validate("124.234.7.9") == True
    assert validate("257.234.7.9") == False
    assert validate("124.275.7.9") == False
