from linked_list import ListNode


def test_has_cycle(solution):
    tail = ListNode(-4)
    cycle = ListNode(2, ListNode(0, tail))
    tail.next = cycle
    head = ListNode(3, cycle)
    assert solution.hasCycle(head)


def test_has_cycle_2(solution):
    temp = ListNode(2)
    head = ListNode(1, temp)
    temp.next = head
    assert solution.hasCycle(head)


def test_has_cycle_3(solution):
    assert not solution.hasCycle(ListNode(1))


def test_has_cycle_edge(solution):
    assert not solution.hasCycle(None)
    assert not solution.hasCycle(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
