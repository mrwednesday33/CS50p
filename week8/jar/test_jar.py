from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12

def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()

    jar.deposit(5)
    assert jar.size == 5

    jar.deposit(7)
    assert jar.size == 12  # Jar is full now

    try:
        jar.deposit(1)  # Should raise ValueError as jar is full
        assert False, "Expected ValueError for depositing more than capacity"
    except ValueError:
        pass

def test_withdraw():
    jar = Jar()

    jar.deposit(10)
    assert jar.size == 10

    jar.withdraw(5)
    assert jar.size == 5

    try:
        jar.withdraw(10)  # Should raise ValueError as jar does not have enough cookies
        assert False, "Expected ValueError for withdrawing more than available"
    except ValueError:
        pass

    try:
        jar.withdraw(-1)  # Should raise ValueError for negative withdraw
        assert False, "Expected ValueError for negative withdraw"
    except ValueError:
        pass

if __name__ == "__main__":
    pytest.main()
