import pytest


@pytest.fixture()
def case1():
    return ([1, 2, 5], 11, 3)


@pytest.fixture()
def case2():
    return ([2], 3, -1)


@pytest.fixture()
def case3():
    return ([1], 0, 0)


def test_coin_change(solution, case1):
    coins, amount, output = case1
    assert solution.coinChange(coins, amount) == output


def test_coin_change_2(solution, case2):
    coins, amount, output = case2
    assert solution.coinChange(coins, amount) == output


def test_coin_change_3(solution, case3):
    coins, amount, output = case3
    assert solution.coinChange(coins, amount) == output
