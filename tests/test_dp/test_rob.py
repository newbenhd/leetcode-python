import pytest


@pytest.mark.parametrize(
    "nums, output",
    [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([2, 7, 9, 3, 1, 5, 2, 6], 22),
        ([1, 2], 2),
        ([1, 3, 1], 3),
    ],
)
def test_rob(solution, nums, output):
    assert solution.rob(nums) == output
