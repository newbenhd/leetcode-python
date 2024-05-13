import pytest

@pytest.mark.parametrize('gas, cost, output', [
    ([1,2,3,4,5], [3,4,5,1,2], 3),
    ([2,3,4],[3,4,3],-1)
])
def test_can_complete_circuit(solution, gas, cost, output):
    assert solution.canCompleteCircuit(gas, cost) == output
