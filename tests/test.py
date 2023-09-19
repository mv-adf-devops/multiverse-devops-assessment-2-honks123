import pytest
from extract import get_input, remove_duplicates, remove_empty_lines, capitalise_names, validate_answer_3

# ticket 1: test that .csv reads successfully into a list

def test_input_is_list():
    # Arrange
    filename = 'results.csv'
    expected_type = list

    # Act
    output = get_input(filename)
    
    # Assert
    assert type(output) == expected_type

# Test header line

def test_list_is_split():
    # Arrange
    filename = 'results.csv'
    expected_header = ['user_id','first_name','last_name','answer_1','answer_2','answer_3']

    # Act
    output = get_input(filename)[0]

    # Assert
    assert output == expected_header

'''

Add functionality to your input script to ignore or remove any duplicate entries
from the input data.
Duplicates are based on the User Id field.
● A final array is created with duplicate entries removed.
● Where duplicates are found, the first entry is retained.

'''

def test_duplicates_removed():

    # Arrange
    filename = 'results.csv'
    data = get_input(filename)
    
    # Act
    test_dedupe = remove_duplicates(data)

    # Make a list of the user IDs from the test_dedupe list
    User_Ids = []
    for i in test_dedupe:
        User_Ids.append(i[0])
    # Now create a set from this list. Sets in Python cannot contain duplicates. In creating the set, duplicates get removed
    User_Id_set = set(User_Ids)
    print(len(User_Id_set))

    # Assert
    # If the number of elements in User_Ids is the sane same as that of User_Id_set, then there were no duplicates
    assert len(User_Ids) == len(User_Id_set)

def test_empty_lines():

    # Arrange
    filename = 'results.csv'
    data = get_input(filename)
    

    # Act
    no_empty_data = remove_empty_lines(data)
    # Define an empty line as a line with a blank first element - i.e. no user ID
    # Check there are no empty lines by cycling through the lines in data and counting any with a blank first element
    emptylines = 0
    for line in no_empty_data:
        if line[0] == '':
            emptylines = emptylines + 1

    # Assert
    assert emptylines == 0

def test_names_capitalised():

    # Arrange
    filename = 'results.csv'
    data = get_input(filename)

    # Act
    capitalised_results = capitalise_names(data)
    # Initialise a counter to count any failed capitalisations
    failures = 0
    for line in capitalised_results:
        if line[1] != line[1].capitalize():
            failures = failures + 1
        if line[2] != line[2].capitalize():
            failures = failures + 1

    # Assert
    assert failures == 0

def test_answer_3():
    # Arrange
    filename = 'results.csv'
    data = get_input(filename)

    # Act
    validated_results = validate_answer_3(data)
    # Initialise a counter to count any answers outside range
    invalid_answers = 0
    for line in validated_results[1:]:
        if int(line[5]) < 1 or int(line[5]) > 10:
            invalid_answers += 1

    # Assert
    assert invalid_answers == 0

def clean_results_exist():
    # Arrange
    
    # Act
    # Assert


