import pytest


@pytest.mark.parametrize(
    "nums, target, output",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 2, 3], 10, []),
    ],
)
def test_two_sum(solution, nums, target, output):
    assert solution.twoSum(nums, target) == output
