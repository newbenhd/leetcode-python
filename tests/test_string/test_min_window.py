import pytest


@pytest.mark.parametrize(
    "s, t, output",
    [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
        ("bba", "ab", "ba"),
        ("aaaaaaaaaaaabbbbbcdd", "abcdd", "abbbbbcdd"),
    ],
)
def test_min_window(solution, s, t, output):
    assert solution.minWindow(s, t) == output
