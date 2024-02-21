import pytest
from p import Solution, TreeNode as Tree, Codec


@pytest.fixture(scope="session")
def solution():
    return Solution()


@pytest.fixture()
def TreeNode():
    return Tree


@pytest.fixture()
def codec():
    return Codec()
