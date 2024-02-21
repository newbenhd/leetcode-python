import pytest


@pytest.fixture
def case1(TreeNode):
    return TreeNode(1, TreeNode(2), TreeNode(3))


@pytest.fixture
def case2(TreeNode):
    return TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))


@pytest.fixture
def case3():
    return None


def test_max_path_sum(solution, case1):
    assert 6 == solution.maxPathSum(case1)


def test_max_path_sum_2(solution, case2):
    assert 42 == solution.maxPathSum(case2)


def test_max_path_sum_3(solution, case3):
    assert 0 == solution.maxPathSum(case3)
