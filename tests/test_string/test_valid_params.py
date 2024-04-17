import pytest


@pytest.mark.parametrize(
    "s, output",
    [
        ("()", True),
        ("(){}[]", True),
        ("(]", False),
        ("[)", False),
        ("[}", False),
        ("]", False),
    ],
)
def test_is_valid(solution, s, output):
    assert solution.isValid(s) == output
