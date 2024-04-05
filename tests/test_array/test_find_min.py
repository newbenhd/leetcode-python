import pytest


@pytest.mark.parametrize(
    "nums, output",
    [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
        ([4, 5, 0, 1, 2, 3], 0),
        ([3, 4, 5, 6, 1, 2], 1),
        ([1], 1),
    ],
)
def test_find_min(solution, nums, output):
    assert solution.findMin(nums) == output
