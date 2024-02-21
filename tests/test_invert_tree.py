import pytest


@pytest.fixture
def case1(TreeNode):
    return (
        TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(7, TreeNode(6), TreeNode(9)),
        ),
        TreeNode(
            4,
            TreeNode(7, TreeNode(9), TreeNode(6)),
            TreeNode(2, TreeNode(3), TreeNode(1)),
        ),
    )


@pytest.fixture
def case2(TreeNode):
    return (
        TreeNode(2, TreeNode(1), TreeNode(3)),
        TreeNode(2, TreeNode(3), TreeNode(1)),
    )


def test_invert_tree(solution, case1):
    input, output = case1
    assert solution.isSameTree(solution.invertTree(input), output)


def test_invert_tree_2(solution, case2):
    input, output = case2
    assert solution.isSameTree(solution.invertTree(input), output)
