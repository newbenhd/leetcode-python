import pytest


@pytest.fixture
def tree(TreeNode):
    return TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))


@pytest.fixture
def tree2(TreeNode):
    return TreeNode(1, right=TreeNode(2))


def test_max_depth(solution, tree):
    assert 3 == solution.maxDepth(tree)


def test_max_depth_2(solution, tree2):
    assert 2 == solution.maxDepth(tree2)
