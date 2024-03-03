import pytest
from heap import Solution, ListNode as Node, Heap as heap


@pytest.fixture()
def solution():
    return Solution()


@pytest.fixture()
def ListNode():
    return Node


@pytest.fixture()
def Heap():
    return heap
