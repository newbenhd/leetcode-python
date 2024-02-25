import pytest


@pytest.fixture
def case1(TreeNode):
    p = TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5)))
    q = TreeNode(8, TreeNode(7), TreeNode(9))
    return (TreeNode(6, p, q), p, q)


@pytest.fixture
def case2(TreeNode):
    q = TreeNode(4, TreeNode(3), TreeNode(5))
    p = TreeNode(2, TreeNode(0), q)
    return (TreeNode(6, p, TreeNode(8, TreeNode(7), TreeNode(9))), p, q)


@pytest.fixture
def case3(TreeNode):
    q = TreeNode(1)
    p = TreeNode(2, q)
    return (p, p, q)


@pytest.fixture
def case4(TreeNode):
    q = TreeNode(9)
    p = TreeNode(8, TreeNode(7), q)
    return (
        TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), p),
        p,
        q,
    )


def test_lca_edge(solution):
    assert solution.lowestCommonAncestor(None, None, None) is None


def test_lca(solution, case1, benchmark):
    root, p, q = case1
    tree = benchmark(solution.lowestCommonAncestor, root, p, q)
    assert solution.isSameTree(root, tree)


def test_lca_2(solution, case2, benchmark):
    root, p, q = case2
    tree = benchmark(solution.lowestCommonAncestor, root, p, q)
    assert solution.isSameTree(p, tree)


def test_lca_3(solution, case3, benchmark):
    root, p, q = case3
    tree = benchmark(solution.lowestCommonAncestor, root, p, q)
    assert solution.isSameTree(tree, root)


def test_lca_4(solution, case4, benchmark):
    root, p, q = case4
    tree = benchmark(solution.lowestCommonAncestor, root, p, q)
    assert solution.isSameTree(tree, p)
