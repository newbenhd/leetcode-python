import pytest
from graph import Solution, Node as node


@pytest.fixture()
def solution():
    return Solution()


@pytest.fixture()
def Node():
    return node
