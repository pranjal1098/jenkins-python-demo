from app import add

def test_add():
    assert add(2, 3) == 5

def test_negative_numbers():
    assert add(-1, -2) == -3