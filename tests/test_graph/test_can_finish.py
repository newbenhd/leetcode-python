import pytest


@pytest.fixture
def case1():
    return (2, [[1, 0]])


@pytest.fixture
def case2():
    return (2, [[1, 0], [0, 1]])


def test_can_finish(solution, case1):
    n, pre = case1
    assert solution.canFinish(n, pre)


def test_can_finish_2(solution, case2):
    n, pre = case2
    assert not solution.canFinish(n, pre)
