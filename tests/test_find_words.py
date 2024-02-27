from collections import Counter
import pytest


@pytest.fixture
def case1():
    return (
        [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ],
        ["oath", "pea", "eat", "rain"],
    )


@pytest.fixture
def case2():
    return ([["a", "b"], ["c", "d"]], ["abcb"])


def test_find_words(solution, case1, benchmark):
    board, words = case1
    output = benchmark(solution.findWords, board, words)
    assert len(output) == 2
    assert Counter(output) == Counter(["eat", "oath"])


def test_find_words_2(solution, case2, benchmark):
    board, words = case2
    assert [] == benchmark(solution.findWords, board, words)
