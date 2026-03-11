from um import count

def test_single():
    assert count("um") == 1
    assert count("um um") == 2

def test_phrase():
    assert count("Um, thanks for the album") == 1
    assert count("Um, thanks, um...") == 2

def test_error():
    assert count("ummm") == 0
