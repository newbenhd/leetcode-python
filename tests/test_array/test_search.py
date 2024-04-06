import pytest


@pytest.mark.parametrize(
    "nums, target, output",
    [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([3, 1], 1, 1),
    ],
)
def test_search(solution, nums, target, output):
    assert solution.search(nums, target) == output


@pytest.mark.parametrize(
    "nums, target, output",
    [([1, 2, 3, 4, 5, 6], 3, 2), ([1, 2, 3, 4, 5, 6], 5, 4), ([1, 2, 3], 1, 0)],
)
def test_binary_search(solution, nums, target, output):
    assert solution.binarySearch(nums, target) == output
