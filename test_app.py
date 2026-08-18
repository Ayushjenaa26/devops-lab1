from app import add, greet

def test_add():
    assert add(2, 3) == 99  # deliberate failure - 2+3=5, not 99

def test_greet():
    assert greet("World") == "Hello, World!"
