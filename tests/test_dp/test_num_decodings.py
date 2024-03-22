import pytest


@pytest.mark.parametrize("s, output", [("12", 2), ("226", 3), ("06", 0), ("12131", 5)])
def test_num_decodings(solution, s, output):
    assert solution.numDecodings(s) == output


@pytest.mark.parametrize("s, output", [("12", 2), ("226", 3), ("06", 0), ("12131", 5)])
def test_num_decodings_recursion(solution, s, output):
    assert solution.numDecodingsRecursion(s) == output


@pytest.mark.perf
def test_num_decodings_recursion_benchmark(solution, benchmark):
    assert benchmark(solution.numDecodingsRecursion, "12131") == 5


@pytest.mark.perf
def test_num_decodings_benchmark(solution, benchmark):
    assert benchmark(solution.numDecodings, "12131") == 5
