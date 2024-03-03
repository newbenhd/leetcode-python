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
def edge1(ListNode):
    # when either a or b becomes None
    a = ListNode(5, ListNode(15, ListNode(10)))
    b = ListNode(1, ListNode(3))
    return (a, b)


@pytest.fixture
def edge2(ListNode):
    a = ListNode(1, ListNode(3))
    b = ListNode(5, ListNode(15, ListNode(10)))
    return (a, b)


@pytest.fixture
def case4(case1, case2):
    a, b = case1
    c, d = case2
    return [a, b, c, d]


def test_merge(solution, case1):
    a, b = case1
    c = solution.merge(a, b)
    assert c.formatStr() == "1,2,3,4,5,7,8,9,13"
    assert c.formatList() == [1, 2, 3, 4, 5, 7, 8, 9, 13]


def test_merge_2(solution, case2):
    a, b = case2
    c = solution.merge(a, b)
    assert c.formatStr() == "2,5,7,8,10,12,15,20"


def test_merge_edge(solution):
    assert solution.merge(None, None) is None


def test_merge_edge_2(solution, edge1):
    a, b = edge1
    c = solution.merge(a, b)
    assert c.formatStr() == "1,3,5,15,10"


def test_merge_edge_3(solution, edge2):
    a, b = edge2
    c = solution.merge(a, b)
    assert c.formatStr() == "1,3,5,15,10"


def test_merge_edge_4(solution, ListNode):
    a, b = None, ListNode(1)
    c = solution.merge(a, b)
    assert c.formatStr() == "1"
    c = solution.merge(b, a)
    assert c.formatStr() == "1"


def test_merge_int(solution):
    assert solution.mergeInt([], []) == []
    assert solution.mergeInt([1], []) == [1]
    assert solution.mergeInt([], [1]) == [1]
    assert solution.mergeInt([1, 3], [2, 5]) == [1, 2, 3, 5]


def test_merge_sort(solution, case3, benchmark):
    assert benchmark(solution.mergeSort, case3) == [3, 9, 10, 27, 38, 43, 82]


def test_merge_sort_2(solution, case4):
    c = solution.mergeKLists(case4)
    assert c.formatStr() == "1,2,2,3,4,5,5,7,7,8,8,9,10,12,13,15,20"


def test_merge_sort_edge(solution):
    assert solution.mergeSort([]) == []


def test_merge_k_list_edge(solution):
    assert solution.mergeKLists([]) is None


def test_merge_k_list_edge_2(solution, ListNode):
    assert solution.mergeKLists([ListNode(1, ListNode(2))]).formatStr() == "1,2"
