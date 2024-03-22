import pytest


@pytest.mark.parametrize("m, n, output", [(3, 7, 28), (3, 2, 3)])
def test_unique_paths(solution, m, n, output):
    assert solution.uniquePaths(m, n) == output
