import pytest


@pytest.mark.parametrize(
    "s, output",
    [("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3), ("", 0), ("abba", 2), ("aab", 2)],
)
def test_length_of_longest_substring(solution, s, output):
    assert solution.lengthOfLongestSubstring(s) == output
