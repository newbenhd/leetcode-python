import pytest


@pytest.mark.parametrize(
    "nums, output",
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
    ],
)
def test_three_sum(solution, nums, output):
    assert solution.threeSum(nums) == output
