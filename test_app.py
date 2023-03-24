import pytest
from extract import read_csv_file

# Ticket 1: Read a CSV file
# In your input script, create a function that will read data from a CSV file.

#Ticket1a: 
def test_input_is_list():
    #Arrange
    filename = "results.csv"
    expected_output = list

    #Act
    output = read_csv_file(filename)

    #Assert
    assert type(output) == expected_output

#Ticket1b
def test_input_is_correct():
    # Arrange
    filename = "results.csv"
    expected_columns = ["user_id","first_name","last_name","answer_1","answer_2","answer_3"]
    expected_rowcount = 25
    
    # Act
    output = read_csv_file(filename)
    actual_columns = output[0]
    actual_rowcount = len(output[1:])

    # Assert
    assert actual_columns == expected_columns
    assert actual_rowcount == expected_rowcount

# Ticket 2: Remove duplicate entries
# Add functionality to your input script to ignore or remove any duplicate entries
# from the input data.
# Duplicates are based on the User Id field.

#Ticket2a: A final array is created with duplicate entries removed.
def test_duplicates_removed():
    pass

#Ticket2b: Where duplicates are found, the first entry is retained.
def test_firstenter_retained():
    pass

# Ticket 3: Ignore empty lines
# Update your input script to ignore any empty lines found when reading in the
# input data file.

#Ticket3a: A final array is created with any empty lines omitted.
def test_inputfile_removeemptylines():
    pass

# Ticket 4: Capitalise user name fields
# Add functionality to your input script to automatically capitalise the first_name
# and last_name fields found in the input data.

#Ticket4a: All names are capitalised in all data entries.
def test_names_capitalised():
    pass

# Ticket 5: Validate the responses to answer 3
# Update your input script to validate the responses to the third answer field.
# This answer must have a numeric value between 1 and 10.
# Any rows with an invalid value are ignored.

#Ticket5a: A final array is created with the input data excluding any rows where
# answer 3 is invalid.
def test_exclude_invalidanswer3():
    pass

#Ticket5b: No answer 3 values will be outside the range of 1 to 10.
def test_answer3_inrange1to10():
    pass

#Ticket 6: Output the cleansed result data to a new file
# Add functionality to your input script to output the cleansed data to a new CSV
# file.

#Ticket6a: A new file is created called clean_results.csv.
def test_newfile_clean_resultscsv():
    pass

#Ticket6b: The file is recreated on each execution.
def test_filecreated_each_execution():
    pass

#Ticket6c: No invalid or unformatted data is present in the new file.
def test_invalid_unformatted_data_removed():
    pass

#Ticket 7: Create an output script
# A new output script will be created which reads in the clean_results.csv CSV
# file and outputs the results to the command line, row by row

#Ticket7a: The script uses the existing sub-module to read the CSV file.
def test_existing_submodule_used():
    pass

#Ticket7b: The printed output will contain all row data and an appropriate header.
def test_row_data_and_headers():
    pass

#Ticket7c: The printed output will be formatted with fixed length strings.
def test_format_fixed_lengthstring():
    pass