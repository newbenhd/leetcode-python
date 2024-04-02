import pytest


@pytest.mark.parametrize(
    "nums, output",
    [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ],
)
def test_contains_duplicate(solution, nums, output):
    assert solution.containsDuplicate(nums) == output
