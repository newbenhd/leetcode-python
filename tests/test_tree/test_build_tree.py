import pytest


@pytest.fixture
def case1():
    return ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])


@pytest.fixture
def case2():
    return ([-1], [-1])


def test_build_tree(solution, case1, TreeNode, benchmark):
    preorder, inorder = case1
    tree = benchmark(solution.buildTree, preorder, inorder)
    assert solution.isSameTree(
        tree,
        TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))),
    )


def test_build_tree_2(solution, case2, TreeNode, benchmark):
    preorder, inorder = case2
    tree = benchmark(solution.buildTree, preorder, inorder)
    assert solution.isSameTree(tree, TreeNode(-1))
