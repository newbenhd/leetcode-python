import pytest


@pytest.fixture()
def case1():
    return ("abcde", "ace", 3)


@pytest.fixture()
def case2():
    return ("abc", "abc", 3)


@pytest.fixture()
def case3():
    return ("abc", "def", 0)


def test_longest_common_subsequence(solution, case1, benchmark):
    text1, text2, output = case1
    assert benchmark(solution.longestCommonSubsequence, text1, text2) == output


def test_longest_common_subsequence_2(solution, case2):
    text1, text2, output = case2
    assert solution.longestCommonSubsequence(text1, text2) == output


def test_longest_common_subsequence_3(solution, case3):
    text1, text2, output = case3
    assert solution.longestCommonSubsequence(text1, text2) == output


def test_longest_common_subsequence_edge(solution):
    assert solution.longestCommonSubsequence("a", "yya") == 1


def test_longest_common_subsequence_edge_2(solution):
    assert solution.longestCommonSubsequence("def", "abcfabcefadeeeaabf") == 3


def test_longest_common_subsequence_recursion(solution, case1, benchmark):
    text1, text2, output = case1
    assert benchmark(solution.longestCommonSubsequenceRecursion, text1, text2) == output
