import pytest


@pytest.mark.parametrize(
    "prices, output", [([7, 1, 5, 3, 6, 4], 5), ([7, 6, 4, 3, 1], 0)]
)
def test_max_profit(solution, prices, output):
    assert solution.maxProfit(prices) == output