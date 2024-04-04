import pytest


@pytest.mark.parametrize("nums, output", [([2, 3, -2, 4], 6), ([-2, 0, -1], 0)])
def test_max_product(solution, nums, output):
    assert solution.maxProduct(nums) == output
