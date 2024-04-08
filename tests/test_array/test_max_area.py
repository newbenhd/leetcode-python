import pytest


@pytest.mark.parametrize(
    "height, output",
    [([1, 8, 6, 2, 5, 4, 8, 3, 7], 49), ([1, 1], 1), ([2, 3, 4, 5, 18, 17, 6], 17)],
)
def test_max_area(solution, height, output):
    assert solution.maxArea(height) == output
