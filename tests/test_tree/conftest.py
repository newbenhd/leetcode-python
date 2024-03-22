import pytest
from tree import Solution, TreeNode as Tree, Codec, Trie as TrieClass, WordDictionary


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


@pytest.fixture()
def Dictionary():
    return WordDictionary
