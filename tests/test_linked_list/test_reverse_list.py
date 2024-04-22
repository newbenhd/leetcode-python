import pytest
from linked_list import ListNodeWithEqual as ListNode


@pytest.mark.parametrize(
    "head, output",
    [
        (
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
            ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1))))),
        ),
        (ListNode(1, ListNode(2)), ListNode(2, ListNode(1))),
        (None, None),
    ],
)
def test_reverse_list(solution, head, output):
    assert solution.reverseList(head) == output


@pytest.mark.parametrize(
    "head, other",
    [(ListNode(1), None), (ListNode(1, ListNode(2)), ListNode(2, ListNode(3)))],
)
def test_list_node_equal(head, other):
    assert head != other
