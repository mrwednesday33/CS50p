from twttr import shorten

def main():
    test_upper_lower_cases()
    test_numbers()

def test_upper_lower_cases():
    assert shorten('twitter') == 'twttr'
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('TwItTeR') == 'TwtTR'

def test_numbers():
    assert shorten('1234') == '1234'

def tes_prunctuation():
    assert shorten('!?.,') == '!?.,'

if __name__ == "__main__":
    main()
