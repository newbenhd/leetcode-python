import pytest


@pytest.mark.parametrize(
    "nums, target, output",
    [([1, 2, 3], 4, 7), ([9], 3, 0), ([-1, 1], 0, 1)],
)
def test_combination_sum(solution, nums, target, output):
    assert solution.combinationSum4(nums, target) == output


@pytest.mark.parametrize(
    "nums, target, output", [([1, 2, 3], 4, 7), ([9], 3, 0), ([-1, 1], 0, 1)]
)
@pytest.mark.skip("not implemented")
def test_combination_sum_recursion(solution, nums, target, output):
    assert solution.combinationSum4Recursion(nums, target) == output


@pytest.mark.perf()
def test_combination_sum_perf(solution, benchmark):
    assert benchmark(solution.combinationSum4, [1, 2, 3], 4) == 7


@pytest.mark.perf()
@pytest.mark.skip("not implemented")
def test_combination_sum_recursion_perf(solution, benchmark):
    assert benchmark(solution.combinationSum4Recursion, [1, 2, 3], 4) == 7
