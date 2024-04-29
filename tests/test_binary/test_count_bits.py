import pytest


@pytest.mark.parametrize("n, output", [(2, [0, 1, 1]), (5, [0, 1, 1, 2, 1, 2])])
def test_count_bits(solution, n, output):
    assert solution.countBits(n) == output
