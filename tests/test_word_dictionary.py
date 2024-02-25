import pytest


@pytest.mark.current
def test_word_dictionary(Dictionary, benchmark):
    word = Dictionary()
    word.addWord("bad")
    word.addWord("dad")
    word.addWord("mad")
    assert not benchmark(word.search, "pad")
    assert word.search("bad")
    assert word.search(".ad")
    assert word.search("b..")
    assert not word.search("...")
