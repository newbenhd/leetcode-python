import pytest


@pytest.mark.parametrize(
    "intervals, newInterval, output",
    [
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        (
            [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            [4, 8],
            [[1, 2], [3, 10], [12, 16]],
        ),
        (
            [[1, 2], [3, 5], [6, 7]],
            [6, 9],
            [[1, 2], [3, 5], [6, 9]],
        ),
    ],
)
def test_insert(solution, intervals, newInterval, output):
    assert solution.insert(intervals, newInterval) == output
