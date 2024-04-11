import pytest


@pytest.mark.parametrize("s, k, output", [("ABAB", 2, 4), ("AABABBA", 1, 4)])
def test_character_replacement(solution, s, k, output):
    assert solution.characterReplacement(s, k) == output
