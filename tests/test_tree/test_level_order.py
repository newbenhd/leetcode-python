import pytest


@pytest.fixture
def case1(TreeNode):
    return TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))


@pytest.fixture
def case2(TreeNode):
    return TreeNode(1)


@pytest.fixture
def case3():
    return None


def test_level_order(solution, case1):
    assert solution.levelOrder(case1) == [[3], [9, 20], [15, 7]]


def test_level_order_2(solution, case2):
    assert solution.levelOrder(case2) == [[1]]


def test_level_order_3(solution, case3):
    assert solution.levelOrder(case3) == []
