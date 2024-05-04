import pytest


@pytest.mark.parametrize(
    "intervals, output",
    [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
    ],
)
def test_merge(intervals, output, solution):
    assert solution.merge(intervals) == output
