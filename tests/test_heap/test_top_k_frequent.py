import pytest


@pytest.fixture()
def case1():
    return [10, 4, 44, 19, 3, 7, 3, 5]


@pytest.fixture()
def case2():
    return [1, 1, 1, 2, 2, 3], 2


@pytest.fixture()
def case3():
    return [1], 1


def test_heap_helper(Heap):
    heap = Heap()
    assert heap.left(0) == 1
    assert heap.right(0) == 2
    assert heap.left(1) == 3
    assert heap.right(2) == 6
    assert heap.parent(6) == 2
    assert heap.left(3) == 7
    assert heap.parent(7) == 3


def test_heap_add(case1, Heap):
    heap = Heap()
    p = case1.pop()
    heap.add((p, p))
    assert heap.pick() == 5
    p = case1.pop()
    heap.add((p, p))
    assert heap.pick() == 5
    p = case1.pop()
    heap.add((p, p))
    assert heap.pick() == 7
    for p in case1:
        heap.add((p, p))
    assert heap.pick() == 44


def test_heap_remove(case1, Heap):
    heap = Heap()
    for p in case1:
        heap.add((p, p))
    assert heap.remove() == (44, 44)
    assert heap.remove() == (19, 19)
    assert heap.remove() == (10, 10)
    assert heap.remove() == (7, 7)
    heap.add((12, 12))
    heap.add((10, 10))
    assert heap.remove() == (12, 12)


def test_top_k_frequent(case2, solution):
    nums, k = case2
    output = solution.topKFrequent(nums, k)
    output.sort()
    assert output == [1, 2]


def test_top_k_frequent_2(case3, solution):
    nums, k = case3
    assert solution.topKFrequent(nums, k) == [1]


def test_top_k_frequent_3(case2, solution):
    nums, k = case2
    output = solution.topKFrequent(nums, k + 100)
    output.sort()
    assert output == [1, 2, 3]
