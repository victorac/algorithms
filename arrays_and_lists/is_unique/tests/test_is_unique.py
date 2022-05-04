import pytest
from arrays_and_lists.is_unique import is_unique, is_unique_brute

TEST_CASES = [
    ("apple", False),
    ("banana", False),
    ("kiwi", False),
    ("pear", True),
    ("", True)
]

@pytest.mark.parametrize("test_input, expected", TEST_CASES)
def test_is_unique(test_input, expected):
    assert is_unique(test_input) == expected

@pytest.mark.parametrize("test_input, expected", TEST_CASES)
def test_is_unique_brute(test_input, expected):
    assert is_unique_brute(test_input) == expected
    
