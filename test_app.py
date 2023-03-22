import pytest
from extract import get_input

def test_input_is_list():
    #Arrange
    filename = "results.csv"
    expected_output = list

    #Act
    output = get_input(filename)

    #Assert
    assert type(output) == expected_output


def test_input_is_correct():
    # Arrange
    filename = "results.csv"
    expected_columns = ["user_id","first_name","last_name","answer_1","answer_2","answer_3"]
    expected_rowcount = 25
    
    # Act
    output = get_input(filename)
    actual_columns = output[0]
    actual_rowcount = len(output[1:])

    # Assert
    assert actual_columns == expected_columns
    assert actual_rowcount == expected_rowcount


def test_input_fails_if_file_not_found():
    pass