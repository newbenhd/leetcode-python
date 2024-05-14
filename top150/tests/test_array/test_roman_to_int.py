import pytest

@pytest.mark.parametrize('s, output', [
                             ('III', 3),
                             ('LVIII', 58),
                             ('MCMXCIV', 1994)
                         ])
def test_roman_to_int(solution, s, output):
    assert solution.romanToInt(s) == output
