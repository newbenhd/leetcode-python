import pytest


@pytest.fixture()
def case1():
    return ([10, 9, 2, 5, 3, 7, 101, 18], 4)


@pytest.fixture()
def case2():
    return ([0, 1, 0, 3, 2, 3], 4)


@pytest.fixture()
def case3():
    return ([7, 7, 7, 7, 7, 7, 7], 1)


def test_length_of_lis(solution, case1):
    assert solution.lengthOfLIS(case1[0]) == case1[1]


def test_length_of_lis_2(solution, case2):
    assert solution.lengthOfLIS(case2[0]) == case2[1]


def test_length_of_lis_3(solution, case3):
    assert solution.lengthOfLIS(case3[0]) == case3[1]
