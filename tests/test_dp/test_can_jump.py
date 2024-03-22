import pytest


@pytest.mark.parametrize(
    "nums, output",
    [([2, 3, 1, 1, 4], True), ([3, 2, 1, 0, 4], False), ([2, 0, 0], True)],
)
def test_can_jump(solution, nums, output):
    assert solution.canJump(nums) == output


@pytest.mark.parametrize(
    "nums, output",
    [([2, 3, 1, 1, 4], True), ([3, 2, 1, 0, 4], False), ([2, 0, 0], True)],
)
def test_can_jump_dp(solution, nums, output):
    assert solution.canJumpDP(nums) == output


@pytest.mark.perf
def test_can_jump_benchmark(solution, benchmark):
    assert benchmark(solution.canJump, [2, 3, 1, 1, 4])


@pytest.mark.perf
def test_can_jump_dp_benchmark(solution, benchmark):
    assert benchmark(solution.canJumpDP, [2, 3, 1, 1, 4])
