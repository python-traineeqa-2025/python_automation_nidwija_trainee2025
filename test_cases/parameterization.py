import pytest

def add(a, b):
    return a + b

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (3, 4, 7),
    (10, 5, 15),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_addition(a, b, expected):
    result = add(a, b)
    assert result == expected
"""
@pytest.mark.parametrize("input_data, expected_output", [
    (input_value_1, expected_value_1),
    (input_value_2, expected_value_2),
    ...
])

"""