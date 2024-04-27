import pytest
from linked_list import ListNodeWithEqual as ListNode


@pytest.mark.parametrize(
    "head, output",
    [
        (
            ListNode(1, ListNode(2, ListNode(3, ListNode(4)))),
            ListNode(1, ListNode(4, ListNode(2, ListNode(3)))),
        ),
        (
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
            ListNode(1, ListNode(5, ListNode(2, ListNode(4, ListNode(3))))),
        ),
    ],
)
def test_reorder_list(solution, head, output):
    solution.reorderList(head)
    assert head == output
