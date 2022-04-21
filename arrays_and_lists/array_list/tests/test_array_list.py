import pytest
from arrays_and_lists.array_list import ArrayList

TEST_CASES = [
        (
            (
                [
                    "apple",
                    "banana",
                ],
                [
                    "passion fruit",
                    "kiwi"
                ]
            ), [
                "apple",
                "banana",
                "passion fruit",
                "kiwi"
            ]
        ),
        (
            [None, None], None
        )
]

@pytest.mark.parametrize("test_input,expected", TEST_CASES)
def test_array_list_add(test_input, expected):
    input_1, input_2 = test_input
    array_1 = ArrayList(input_1)
    array_2 = ArrayList(input_2)
    array_3 = array_1 + array_2
    assert array_3 == ArrayList(expected)


TEST_CASES = [
    (
        ([
            "apple",
            "banana",
        ], 0),
        "apple"
    ),
        (
        ([
            "apple",
            "banana",
        ], 1),
        "banana"
    )
]
@pytest.mark.parametrize("test_input,expected", TEST_CASES)
def test_array_list_get(test_input, expected):
    input_1, index = test_input
    array_1 = ArrayList(input_1)
    assert array_1[index] == expected
