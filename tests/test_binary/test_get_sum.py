import pytest


@pytest.mark.parametrize("a, b, output", [(1, 2, 3), (2, 3, 5)])
def test_get_sum(solution, a, b, output):
    assert solution.getSum(a, b) == output
