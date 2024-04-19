import pytest


@pytest.mark.parametrize(
    "s, output",
    [("babad", "bab"), ("cbbd", "bb"), ("a", "a"), ("abb", "bb"), ("eabcb", "bcb")],
)
def test_longest_palindrome(solution, s, output):
    assert solution.longestPalindrome(s) == output
