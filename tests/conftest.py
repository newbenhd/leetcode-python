import pytest
from p import Solution, TreeNode as Tree, Codec, Trie as TrieClass


@pytest.fixture(scope="session")
def solution():
    return Solution()


@pytest.fixture()
def TreeNode():
    return Tree


@pytest.fixture()
def codec():
    return Codec()


@pytest.fixture()
def Trie():
    return TrieClass
