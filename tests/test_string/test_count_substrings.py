import pytest


@pytest.mark.parametrize("s, output", [("abc", 3), ("aaa", 6)])
def test_count_substrings(solution, s, output):
    assert solution.countSubstrings(s) == output
