import pytest


@pytest.mark.parametrize(
    "nums, output",
    [([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6), ([1], 1), ([5, 4, -1, 7, 8], 23)],
)
def test_max_subarray(solution, nums, output):
    assert solution.maxSubArray(nums) == output
