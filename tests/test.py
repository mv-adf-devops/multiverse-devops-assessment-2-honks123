import pytest
from extract import get_input

# ticket 1: test that .csv reads successfully into a list

def test_input_is_list():
    # Arrange
    filename = 'results.csv'
    expected_type = list

    # Act
    output = get_input(filename)

    # read_csv
    
    # Assert
    assert type(output) == expected_type
