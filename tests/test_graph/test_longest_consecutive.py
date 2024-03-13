import pytest


@pytest.fixture()
def case1():
    return ([100, 4, 200, 1, 3, 2], 4)


@pytest.fixture()
def case2():
    return ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9)


@pytest.fixture()
def case3():
    return ([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6], 7)


def test_longest_consecutive(solution, case1):
    input, output = case1
    assert solution.longestConsecutive(input) == output


def test_longest_consecutive_2(solution, case2):
    input, output = case2
    assert solution.longestConsecutive(input) == output


def test_longest_consecutive_3(solution, case3):
    input, output = case3
    assert solution.longestConsecutive(input) == output
