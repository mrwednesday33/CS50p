import pytest
from datetime import date, timedelta
from seasons import calculate_age_in_minutes, format_minutes_to_words

def test_calculate_age_in_minutes():
    # Test with a date two years ago
    birth_date = date.today().replace(year=date.today().year - 2)
    assert calculate_age_in_minutes(birth_date) == 2 * 365 * 24 * 60

    # Test with a date 10 years ago
    birth_date = date.today().replace(year=date.today().year - 10)
    assert calculate_age_in_minutes(birth_date) == 10 * 365 * 24 * 60

    # Test with a date 100 years ago
    birth_date = date.today().replace(year=date.today().year - 100)
    assert calculate_age_in_minutes(birth_date) == 100 * 365 * 24 * 60

    # Test with a date in the future
    birth_date = date.today().replace(year=date.today().year + 1)
    assert calculate_age_in_minutes(birth_date) == 0

def test_format_minutes_to_words():
    assert format_minutes_to_words(1) == "one"
    assert format_minutes_to_words(10) == "ten"
    assert format_minutes_to_words(100) == "one hundred"
    assert format_minutes_to_words(1000) == "one thousand"
    assert format_minutes_to_words(10000) == "ten thousand"
    assert format_minutes_to_words(123456) == "one hundred twenty-three thousand four hundred fifty-six"

def test_calculate_age_in_minutes_leap_year():
    # Test with a birth date on a leap year
    birth_date = date(2000, 2, 29)
    today = date.today()
    expected_age = (today - date(today.year, 1, 1)).days * 24 * 60
    assert calculate_age_in_minutes(birth_date) == expected_age

if __name__ == "__main__":
    pytest.main()
