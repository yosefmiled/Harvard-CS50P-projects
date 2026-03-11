from seasons import check_birthday

def test_check_birthday():
    assert check_birthday('2008-12-17') == ('2008', '12', '17')
    assert check_birthday('1689-9-7') == None
    assert check_birthday('december 12, 2008') == None


