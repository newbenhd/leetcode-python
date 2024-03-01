import pytest
from heap import Solution, ListNode as Node


@pytest.fixture()
def solution():
    return Solution()


@pytest.fixture()
def ListNode():
    return Node
