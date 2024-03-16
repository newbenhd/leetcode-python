import pytest


@pytest.mark.parametrize(
    "s, wordDict, output",
    [
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
        ("", ["apple"], True),
    ],
)
def test_word_break(solution, s, wordDict, output):
    assert solution.wordBreak(s, wordDict) == output


@pytest.mark.parametrize(
    "s, wordDict, output", [("applepenapple", ["apple", "pen"], True)]
)
@pytest.mark.perf
def test_word_break_perf(solution, s, wordDict, output, benchmark):
    assert benchmark(solution.wordBreak, s, wordDict) == output


@pytest.mark.parametrize(
    "s, wordDict, output",
    [
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
        ("", ["apple"], True),
    ],
)
def test_word_break_recursion(solution, s, wordDict, output):
    assert solution.wordBreakRecursion(s, wordDict) == output


@pytest.mark.parametrize(
    "s, wordDict, output", [("applepenapple", ["apple", "pen"], True)]
)
@pytest.mark.perf
def test_word_break_recursion_perf(solution, s, wordDict, output, benchmark):
    assert benchmark(solution.wordBreakRecursion, s, wordDict) == output
