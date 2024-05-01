import pytest


@pytest.mark.parametrize(
    "nums, output", [([3, 0, 1], 2), ([0, 1], 2), ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8)]
)
def test_missing_number(solution, nums, output):
    assert solution.missingNumber(nums) == output
