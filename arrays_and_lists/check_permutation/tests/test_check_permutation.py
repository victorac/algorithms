import pytest
from arrays_and_lists.check_permutation import check_permutation, check_permutation_brute

TEST_CASES = [
    (("abc", "cba"), True),
    (("absdalkjqweoi", "alkabsweoidjq"), True),
    (("asdf", "asdfg"), False),
    (("", "abd"), False),
    (("", ""), True)
]

@pytest.mark.parametrize("test_input, expected", TEST_CASES)
def test_check_permutation(test_input, expected):
    assert check_permutation(*test_input) == expected

@pytest.mark.parametrize("test_input, expected", TEST_CASES)
def test_check_permutation_brute(test_input, expected):
    assert check_permutation_brute(*test_input) == expected