import pytest
from linked_list import ListNodeWithEqual as ListNode


@pytest.mark.parametrize(
    "head, n, output",
    [
        (
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
            2,
            ListNode(1, ListNode(2, ListNode(3, ListNode(5)))),
        ),
        (ListNode(1), 1, None),
        (ListNode(1, ListNode(2)), 1, ListNode(1)),
        (ListNode(1, ListNode(2)), 2, ListNode(2)),
    ],
)
def test_remove_nth_from_end(head, n, output, solution):
    assert solution.removeNthFromEnd(head, n) == output


@pytest.mark.parametrize(
    "head, n, output",
    [
        (
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
            2,
            ListNode(1, ListNode(2, ListNode(3, ListNode(5)))),
        ),
        (ListNode(1), 1, None),
        (ListNode(1, ListNode(2)), 1, ListNode(1)),
        (ListNode(1, ListNode(2)), 2, ListNode(2)),
    ],
)
def test_remove_nth_from_end_stack(head, n, output, solution):
    assert solution.removeNthFromEndStack(head, n) == output
