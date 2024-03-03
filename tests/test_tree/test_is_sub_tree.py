import pytest


@pytest.fixture
def case1(TreeNode):
    return (
        TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5)),
        TreeNode(4, TreeNode(1), TreeNode(2)),
    )


@pytest.fixture
def case2(TreeNode):
    return (
        TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5)),
        TreeNode(4, TreeNode(1), TreeNode(2)),
    )


@pytest.fixture
def case3(TreeNode):
    return (TreeNode(1), None)


def test_is_sub_tree(solution, case1):
    root, subRoot = case1
    assert solution.isSubtree(root, subRoot)


def test_is_sub_tree_2(solution, case2):
    root, subRoot = case2
    assert not solution.isSubtree(root, subRoot)


def test_is_sub_tree_3(solution, case3):
    root, subRoot = case3
    assert solution.isSubtree(root, subRoot)
