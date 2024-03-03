import pytest


@pytest.fixture
def case1(TreeNode):
    return TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))


@pytest.fixture
def case2():
    return None


@pytest.fixture
def case3(TreeNode):
    return TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))), TreeNode(5))


def test_tree_serialize(codec, case1, solution):
    data = codec.serialize(case1)
    assert isinstance(data, str)
    tree = codec.deserialize(data)
    assert not tree == case1
    assert solution.isSameTree(tree, case1)


def test_tree_serialize2(codec, case2, solution):
    data = codec.serialize(case2)
    assert isinstance(data, str)
    tree = codec.deserialize(data)
    assert tree == case2
    assert solution.isSameTree(tree, case2)


def test_tree_serialize_3(codec, case3, solution):
    data = codec.serialize(case3)
    assert isinstance(data, str)
    tree = codec.deserialize(data)
    assert not tree == case3
    assert solution.isSameTree(tree, case3)
