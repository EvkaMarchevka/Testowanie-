import file3


def test_add():
    assert file3.add(7, 3) == 10
    assert file3.add(7, -1) == 6
    assert file3.add(-4, 0) == -4
    assert file3.add(20, 30) >= 50

def test_multiply():
    assert file3.multiply(7, 3) == 21
    assert file3.multiply(7, -1) == -7
    assert file3.multiply(-4, 0) == 0
    assert file3.multiply(20, 30) >= 50

def test_invert_string():
    assert file3.invert_string("") == ""
    assert file3.invert_string("abc") == "cba"

def test_is_palilndrom():
    assert  file3.is_palindrom('ala') == "True "

def test_

test_add()
test_multiply()


