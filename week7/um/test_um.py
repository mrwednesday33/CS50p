from um import count


def test_count():
    # Test cases with different variations of "um"
    assert count("hello, um, world") == 1
    assert count("um hello um um") == 3
    assert count("UM is not the same as um") == 2
    assert count("Um, um, um") == 3

    # Test cases with words containing "um" but not standalone "um"
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("crumb") == 0

    # Test case with no "um"
    assert count("Hello, world!") == 0


if __name__ == "__main__":
    test_count()
