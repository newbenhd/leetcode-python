import pytest


@pytest.mark.parametrize(
    "s, output",
    [("A man, a plan, a canal: Panama", True), ("race a car", False), (" ", True)],
)
def test_is_palindrome(s, output, solution):
    assert solution.isPalindrome(s) == output
