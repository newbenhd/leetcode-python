import pytest


@pytest.mark.parametrize(
    "nums, output",
    [
        ([2, 3, 2], 3),
        ([1, 2, 3, 1], 4),
        ([1, 2, 3], 3),
        ([1, 2, 3, 1, 5, 2, 2], 10),
        ([1, 1, 1, 2], 3),
        ([3], 3),
    ],
)
def test_rob(solution, nums, output):
    assert solution.rob2(nums) == output
