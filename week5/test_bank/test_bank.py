from bank import value

def test_value_hello():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("hello there") == 0

def test_value_h():
    assert value("Hi") == 20
    assert value("hi") == 20
    assert value("HI") == 20
    assert value("hey") == 20

def test_value_other():
    assert value("What's up") == 100
    assert value("Goodbye") == 100
    assert value("") == 100
    assert value("   ") == 100
