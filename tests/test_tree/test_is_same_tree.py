import pytest


@pytest.fixture
def case1(TreeNode):
    return (
        TreeNode(1, TreeNode(2), TreeNode(3)),
        TreeNode(1, TreeNode(2), TreeNode(3)),
    )


@pytest.fixture
def case2(TreeNode):
    return (TreeNode(1, TreeNode(2)), TreeNode(1, right=TreeNode(2)))


@pytest.fixture
def case3(TreeNode):
    return (
        TreeNode(1, TreeNode(2), TreeNode(1)),
        TreeNode(1, TreeNode(1), TreeNode(2)),
    )


def test_is_same_tree(solution, case1, benchmark):
    p, q = case1
    assert benchmark(solution.isSameTree, p, q)


def test_is_same_tree_2(solution, case2, benchmark):
    p, q = case2
    assert not benchmark(solution.isSameTree, p, q)


def test_is_same_tree_3(solution, case3, benchmark):
    p, q = case3
    assert not benchmark(solution.isSameTree, p, q)
