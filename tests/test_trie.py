def test_trie(Trie, benchmark):
    trie = Trie()
    trie.insert("apple")
    assert benchmark(trie.search, "apple")
    assert not trie.search("app")


def test_trie_2(Trie, benchmark):
    trie = Trie()
    trie.insert("apple")
    assert trie.startsWith("app")
    trie.insert("app")
    assert benchmark(trie.search, "app")


def test_trie_3(Trie):
    trie = Trie()
    trie.insert("apple")
    assert not trie.search("ape")
    assert not trie.startsWith("ape")
