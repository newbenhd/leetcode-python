import pytest
from linked_list import ListNodeWithEqual as ListNode


@pytest.mark.parametrize(
    "lists, output",
    [
        (
            [
                ListNode(1, ListNode(4, ListNode(5))),
                ListNode(1, ListNode(3, ListNode(4))),
                ListNode(2, ListNode(6)),
            ],
            ListNode(
                1,
                ListNode(
                    1,
                    ListNode(
                        2,
                        ListNode(3, ListNode(4, ListNode(4, ListNode(5, ListNode(6))))),
                    ),
                ),
            ),
        ),
        ([], None),
        ([None], None),
    ],
)
def test_merge_k_lists(solution, lists, output):
    assert solution.mergeKLists(lists) == output


@pytest.mark.parametrize(
    "lists, output",
    [
        (
            [
                ListNode(1, ListNode(4, ListNode(5))),
                ListNode(1, ListNode(3, ListNode(4))),
                ListNode(2, ListNode(6)),
            ],
            ListNode(
                1,
                ListNode(
                    1,
                    ListNode(
                        2,
                        ListNode(3, ListNode(4, ListNode(4, ListNode(5, ListNode(6))))),
                    ),
                ),
            ),
        ),
        ([], None),
        ([None], None),
    ],
)
def test_merge_k_lists_binary(solution, lists, output):
    assert solution.mergeKListsBinary(lists) == output


@pytest.mark.timeout(10)
@pytest.mark.skip("benchmark somehow gives falsy. need investigation")
def test_merge_k_lists_bench(solution, benchmark):
    assert benchmark(
        solution.mergeKLists,
        [
            ListNode(1, ListNode(4, ListNode(5))),
            ListNode(1, ListNode(3, ListNode(4))),
            ListNode(2, ListNode(6)),
        ],
    ) == ListNode(
        1,
        ListNode(
            1,
            ListNode(
                2,
                ListNode(3, ListNode(4, ListNode(4, ListNode(5, ListNode(6))))),
            ),
        ),
    )


@pytest.mark.timeout(10)
@pytest.mark.skip("benchmark somehow gives falsy. need investigation")
def test_merge_k_lists_binary_bench(solution, benchmark):
    assert benchmark(
        solution.mergeKListsBinary,
        [
            ListNode(1, ListNode(4, ListNode(5))),
            ListNode(1, ListNode(3, ListNode(4))),
            ListNode(2, ListNode(6)),
        ],
    ) == ListNode(
        1,
        ListNode(
            1,
            ListNode(
                2,
                ListNode(3, ListNode(4, ListNode(4, ListNode(5, ListNode(6))))),
            ),
        ),
    )
