import pytest


@pytest.mark.parametrize(
    "nums, output",
    [([1, 2, 3, 4], [24, 12, 8, 6]), ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0])],
)
def test_product_except_self(solution, nums, output):
    assert solution.productExceptSelf(nums) == output
