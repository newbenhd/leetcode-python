import pytest


@pytest.fixture
def case1(ListNode):
    a = ListNode(1, ListNode(2, ListNode(5, ListNode(7))))
    b = ListNode(3, ListNode(4, ListNode(8, ListNode(9, ListNode(13)))))
    return (a, b)


@pytest.fixture
def case2(ListNode):
    a = ListNode(2, ListNode(7, ListNode(8, ListNode(10, ListNode(12, ListNode(15))))))
    b = ListNode(5, ListNode(20))
    return (a, b)


@pytest.fixture
def case3():
    return [38, 27, 43, 3, 9, 82, 10]


@pytest.fixture
def case4(case1, case2):
    a, b = case1
    c, d = case2
    return [a, b, c, d]


def test_merge(solution, case1):
    a, b = case1
    c = solution.merge(a, b)
    assert c.formatStr() == "1,2,3,4,5,7,8,9,13"


def test_merge_2(solution, case2):
    a, b = case2
    c = solution.merge(a, b)
    assert c.formatStr() == "2,5,7,8,10,12,15,20"


@pytest.mark.heap
def test_merge_sort(solution, case3, benchmark):
    assert benchmark(solution.mergeSort, case3) == [3, 9, 10, 27, 38, 43, 82]


@pytest.mark.heap
def test_merge_sort_2(solution, case4):
    c = solution.mergeKLists(case4)
    assert c.formatStr() == "1,2,2,3,4,5,5,7,7,8,8,9,10,12,13,15,20"
