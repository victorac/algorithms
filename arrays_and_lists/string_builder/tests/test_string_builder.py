import pytest
from arrays_and_lists.string_builder import StringBuilder

TEST_CASES = [
        (
            [
                "apple",
                "banana",
                "passion fruit",
                "kiwi"
            ], "applebananapassion fruitkiwi"
        ),
        (
            [], ""
        )
]

@pytest.mark.parametrize("test_input,expected", TEST_CASES)
def test_string_builder(test_input, expected):
    builder = StringBuilder()
    for word in test_input:
        builder.append(word)
    assert builder.to_string() == expected