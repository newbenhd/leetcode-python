import pytest


@pytest.fixture()
def case1():
    return (2, 2)


@pytest.fixture()
def case2():
    return (3, 3)


@pytest.fixture()
def case3():
    return (4, 5)


@pytest.fixture()
def case4():
    return (5, 8)


@pytest.fixture()
def large_case():
    return (10, 89)


def test_climb_stairs(solution, case1):
    input, output = case1
    assert solution.climbStairs(input) == output


def test_climb_stairs_2(solution, case2, case3, case4):
    input, output = case2
    assert solution.climbStairs(input) == output
    input, output = case3
    assert solution.climbStairs(input) == output
    input, output = case4
    assert solution.climbStairs(input) == output


def test_climb_stairs_3(solution, large_case, benchmark):
    input, output = large_case
    assert benchmark(solution.climbStairs, input) == output


def test_climb_stairs_edge(solution):
    assert solution.climbStairs(1) == 1
