import number_checker as num

def test_check_even():
    inp = 12
    result = num.check_even_odd(inp)
    assert result == 0

def test_check_odd():
    inp = 11
    result = num.check_even_odd(inp)
    assert result == 1