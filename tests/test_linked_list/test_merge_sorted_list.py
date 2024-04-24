import pytest
from linked_list import ListNodeWithEqual as ListNode


@pytest.mark.parametrize(
    "list1, list2, output",
    [
        (
            ListNode(1, ListNode(2, ListNode(4))),
            ListNode(1, ListNode(3, ListNode(4))),
            ListNode(
                1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4)))))
            ),
        ),
        (None, None, None),
        (None, ListNode(0), ListNode(0)),
        (ListNode(1, ListNode(2)), None, ListNode(1, ListNode(2))),
        (
            ListNode(2, ListNode(5)),
            ListNode(1, ListNode(3)),
            ListNode(1, ListNode(2, ListNode(3, ListNode(5)))),
        ),
        (
            ListNode(2),
            ListNode(1, ListNode(3, ListNode(4))),
            ListNode(1, ListNode(2, ListNode(3, ListNode(4)))),
        ),
    ],
)
def test_merge_two_lists(solution, list1, list2, output):
    assert solution.mergeTwoLists(list1, list2) == output


@pytest.mark.parametrize(
    "list1, list2, output",
    [
        (
            ListNode(1, ListNode(2, ListNode(4))),
            ListNode(1, ListNode(3, ListNode(4))),
            ListNode(
                1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4)))))
            ),
        ),
        (None, None, None),
        (None, ListNode(0), ListNode(0)),
        (ListNode(1, ListNode(2)), None, ListNode(1, ListNode(2))),
        (
            ListNode(2, ListNode(5)),
            ListNode(1, ListNode(3)),
            ListNode(1, ListNode(2, ListNode(3, ListNode(5)))),
        ),
        (
            ListNode(2),
            ListNode(1, ListNode(3, ListNode(4))),
            ListNode(1, ListNode(2, ListNode(3, ListNode(4)))),
        ),
    ],
)
def test_merge_two_lists_recursion(solution, list1, list2, output):
    assert solution.mergeTwoListsRecursive(list1, list2) == output


# def test_merge_two_lists_bench(solution, benchmark):
#     assert benchmark(
#         solution.mergeTwoLists, ListNode(1, ListNode(3)), ListNode(2, ListNode(4))
#     ) == ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
#
#
# def test_merge_twoLists_recursive_bench(solution, benchmark):
#     assert benchmark(
#         solution.mergeTwoListsRecursive,
#         ListNode(1, ListNode(3)),
#         ListNode(2, ListNode(4)),
#     ) == ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
