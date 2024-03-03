import pytest
from heap import Solution, ListNode as Node, Heap as heap, MedianFinder as MFinder


@pytest.fixture()
def solution():
    return Solution()


@pytest.fixture()
def ListNode():
    return Node


@pytest.fixture()
def Heap():
    return heap


@pytest.fixture()
def MedianFinder():
    return MFinder
