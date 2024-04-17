import pytest


@pytest.mark.parametrize(
    "s, t, output",
    [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("abcd", "abc", False),
        ("abc", "aabc", False),
    ],
)
def test_valid_anagram(solution, s, t, output):
    assert solution.isAnagram(s, t) == output
    assert solution.isAnagram2(s, t) == output


@pytest.mark.parametrize("s, t, output", [("anagram", "nagaram", True)])
def test_valid_anagram_benchmark(solution, s, t, output, benchmark):
    assert benchmark(solution.isAnagram, s, t) == output


@pytest.mark.parametrize("s, t, output", [("anagram", "nagaram", True)])
def test_valid_anagram_2_benchmark(solution, s, t, output, benchmark):
    assert benchmark(solution.isAnagram2, s, t) == output
