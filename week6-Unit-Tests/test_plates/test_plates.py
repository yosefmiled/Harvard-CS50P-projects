from plates import is_valid

def test_two_letters():
    assert is_valid("as135") == True
    assert is_valid("jfjgf") == True
    assert is_valid("HJBF") == True

def test_n_characters():
    assert is_valid("wwyf2647") == False
    assert is_valid("h") == False

def test_numbers():
    assert is_valid("ghr45g") == False
    assert is_valid("hdf45") == True
    assert is_valid("6756") == False

def test_zero():
    assert is_valid("0uejg") == False
    assert is_valid("uejg04") == False
def test_punctuation():
    assert is_valid("jdf k") == False
    assert is_valid("hnbf.h") == False
    assert is_valid("jcf!?") == False
