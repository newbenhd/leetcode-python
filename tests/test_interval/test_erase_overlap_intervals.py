import pytest
@pytest.mark.parametrize("intervals, output", [
  ( [[1,2],[2,3],[3,4],[1,3]], 1),
  ([[1,2],[1,2],[1,2]], 2),
  ([[1,2],[2,3]], 0)
])
def test_erase_overlap_intervals(solution, intervals, output):
  assert solution.eraseOverlapIntervals(intervals) == output
