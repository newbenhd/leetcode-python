import pytest


@pytest.mark.parametrize("n, output", [(11, 3), (128, 1), (2147483645, 30)])
def test_hamming_weight(solution, n, output):
    assert solution.hammingWeight(n) == output
