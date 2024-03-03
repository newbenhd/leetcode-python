import pytest


@pytest.fixture
def case1(TreeNode):
    return (TreeNode(3, TreeNode(1, right=TreeNode(2)), TreeNode(4)), 1)


@pytest.fixture
def case2(TreeNode):
    return (
        TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6)),
        3,
    )


def test_kth_smallest(solution, case1, benchmark):
    root, k = case1
    assert 1 == benchmark(solution.kthSmallest, root, k)


def test_kth_smallest_2(solution, case2, benchmark):
    root, k = case2
    assert 3 == benchmark(solution.kthSmallest, root, k)
