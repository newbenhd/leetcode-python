import pytest


@pytest.fixture()
def case1():
    return (
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ],
        1,
    )


@pytest.fixture()
def case2():
    return (
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ],
        3,
    )


def test_num_islands(solution, case1):
    input, output = case1
    assert solution.numIslands(input) == output


def test_num_islands_2(solution, case2):
    input, output = case2
    assert solution.numIslands(input) == output


def test_num_islands_edge(solution):
    assert solution.numIslands([["1"], ["0"]]) == 1
    assert solution.numIslands([["0"]]) == 0
