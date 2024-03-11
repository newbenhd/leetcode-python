import pytest


@pytest.fixture()
def case1():
    return [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]


@pytest.fixture()
def case2():
    return [[1]]


def test_pacific_atlantic(solution, case1):
    result = sorted(solution.pacificAtlantic(case1))
    assert result == [
        [0, 4],
        [1, 3],
        [1, 4],
        [2, 2],
        [3, 0],
        [3, 1],
        [4, 0],
    ]


def test_pacific_atlantic_2(solution, case2):
    assert solution.pacificAtlantic(case2) == [[0, 0]]


def test_pacific_atlantic_v2(solution, case1):
    result = sorted(solution.pacificAtlantic_v2(case1))
    assert result == [
        [0, 4],
        [1, 3],
        [1, 4],
        [2, 2],
        [3, 0],
        [3, 1],
        [4, 0],
    ]


def test_pacific_atlantic_v2_2(solution, case2):
    assert solution.pacificAtlantic_v2(case2) == [[0, 0]]
