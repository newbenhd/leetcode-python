import pytest


@pytest.mark.parametrize(
    "nums, target, output",
    [([1, 2, 3], 4, 7), ([9], 3, 0), ([-1, 1], 0, 1)],
)
def test_combination_sum(solution, nums, target, output):
    assert solution.combinationSum4(nums, target) == output


@pytest.mark.perf()
def test_combination_sum_perf(solution, benchmark):
    assert benchmark(solution.combinationSum4, [1, 2, 3], 4) == 7
