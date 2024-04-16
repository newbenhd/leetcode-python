import pytest


@pytest.mark.parametrize(
    "strs, output",
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        ),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ],
)
def test_group_anagrams(solution, strs, output):
    assert solution.groupAnagrams(strs) == output
