import pytest


@pytest.fixture()
def case1(Node):
    a, b, c, d = Node(1), Node(2), Node(3), Node(4)
    a.neighbors = [b, d]
    b.neighbors = [a, c]
    c.neighbors = [b, d]
    d.neighbors = [a, c]
    return a


def test_clone_graph(case1, solution, benchmark):
    assert case1.fmtList() == [[2, 4], [1, 3], [2, 4], [1, 3]]
    cloned = benchmark(solution.cloneGraph, case1)
    assert cloned.fmtList() == [[2, 4], [1, 3], [2, 4], [1, 3]]
    assert cloned.fmtList() == case1.fmtList()
    assert cloned != case1


def test_clone_graph_edge(solution, Node):
    node = Node(1)
    assert node.fmtList() == [[]]
    cloned = solution.cloneGraph(node)
    assert cloned.fmtList() == [[]]
    assert cloned.fmtList() == node.fmtList()
    assert cloned != node


def test_clone_graph_edge_2(solution):
    assert solution.cloneGraph(None) is None
