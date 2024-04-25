import pytest


@pytest.mark.parametrize(
    "citations, output",
    [([3, 0, 6, 1, 5], 3), ([1, 3, 1], 1), ([1], 1), ([], 0), ([0, 0, 0, 2], 1)],
)
def test_h_index(solution, citations, output):
    assert solution.hIndex(citations) == output


@pytest.mark.parametrize(
    "citations, output",
    [([3, 0, 6, 1, 5], 3), ([1, 3, 1], 1), ([1], 1), ([], 0), ([0, 0, 0, 2], 1)],
)
def test_h_index_sort(solution, citations, output):
    assert solution.hIndexSort(citations) == output
