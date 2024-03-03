import pytest


@pytest.fixture
def case1(TreeNode):
    return TreeNode(2, TreeNode(1), TreeNode(3))


@pytest.fixture
def case2(TreeNode):
    return TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))


@pytest.fixture
def case3():
    return None


def test_is_valid_bst(solution, case1, benchmark):
    assert benchmark(solution.isValidBST, case1)


def test_is_valid_bst_2(solution, case2, benchmark):
    assert not benchmark(solution.isValidBST, case2)


def test_is_valid_bst_3(solution, case3, benchmark):
    assert benchmark(solution.isValidBST, case3)
