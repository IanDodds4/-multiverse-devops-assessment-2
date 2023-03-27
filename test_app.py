import pytest
import csv
import os
import subprocess

import io
import sys
from contextlib import redirect_stdout

from extract import read_csv_file

# Ticket 1: Read a CSV file
# In your input script, create a function that will read data from a CSV file.

# Ticket1a: 
def test_input_is_list():
    
    #Arrange
    filename = "results.csv"
    expected_output = list

    #Act
    output = read_csv_file(filename)

    #Assert
    assert type(output) == expected_output

# Ticket1b
def test_input_is_correct():
    
    # Arrange
    filename = "results.csv"
    expected_columns = ["1","Charissa","Clark","yes","c","7"]
    expected_rowcount = 26
    
    # Act
    output = read_csv_file(filename)
    actual_columns = output[0]
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        actual_rowcount = len(rows)

    # Assert
    assert actual_columns == expected_columns
    assert actual_rowcount == expected_rowcount

# Ticket 2: Remove duplicate entries
# Add functionality to your input script to ignore or remove any duplicate entries
# from the input data.
# Duplicates are based on the User Id field.

# Ticket2a: A final array is created with duplicate entries removed.
def test_duplicates_removed():
    
    # Arrange
    filename = "clean_results.csv"
    column_name = "user_id" # As user_id is the primary key for the dataset, this will be used for testing duplicates
    seen_ids = set()

    # Act
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
                user_id = row[column_name]
                if user_id in seen_ids:
                    actual = False
                    break
                else:
                    seen_ids.add(user_id)
        else:
            actual = True

    # Assert
    assert actual, f"CSV file contains duplicates in column '{column_name}'."

# Ticket2b: Where duplicates are found, the first entry is retained.

def test_firstentery_retained():
    
    # Arrange
    filename = "clean_results.csv"
    expected_columns_example1 = ["6","Abra","Sheppard","yes","b","6"]
    expected_columns_example2 = ["17","Dieter","Alvarado","yes","b","6"]
    
    # Act
    output = read_csv_file(filename)
    actual_columns_example1 = output[4]
    actual_columns_example2 = output[13]

    # Assert
    assert expected_columns_example1 == actual_columns_example1
    assert expected_columns_example2 == actual_columns_example2

# Ticket 3: Ignore empty lines
# Update your input script to ignore any empty lines found when reading in the input data file.

# Ticket3a: A final array is created with any empty lines omitted.

def test_removeemptylines():
        
    # Arrange
    filename = "clean_results.csv"
    empty_row = False
    
    # Act
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if not row:
                empty_row = True
                break

    # Assert
    assert not empty_row, "clean_results.csv file contains empty rows."

# Ticket 4: Capitalise user name fields
# Add functionality to your input script to automatically capitalise the first_name and last_name fields found in the input data.

# Ticket4a: All names are capitalised in all data entries.
def test_names_capitalised():
        
    # Arrange
    filename = "clean_results.csv"
    first_col = []
    last_col = []
    
    # Act
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            first_col.append(row["first_name"])
            last_col.append(row["last_name"])

    # Assert
    for name in first_col:
        assert name[0].isupper(), f"{name} does not have capatalised first letter."
    for name in last_col:
        assert name[0].isupper(), f"{name} does not have capatalised first letter."

# Ticket 5: Validate the responses to answer 3
# Update your input script to validate the responses to the third answer field.
# This answer must have a numeric value between 1 and 10.
# Any rows with an invalid value are ignored.

# Ticket5a: No answer 3 values will be outside the range of 1 to 10.
def test_answer3_inrange1to10():
            
    # Arrange
    filename = "clean_results.csv"
    answer_3_col = []
    
    # Act
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            answer_3_col.append(row["answer_3"])

    # Assert
    for answer in answer_3_col:
        assert 1 <= int(answer) <= 10, f"{answer} is not between 1 and 10."


# Ticket 6: Output the cleansed result data to a new file
# Add functionality to your input script to output the cleansed data to a new CSV
# file.

# Ticket6a: A new file is created called clean_results.csv.
def test_newfile_clean_resultscsv():
                
    # Arrange
    expected_filename = "clean_results.csv"
    
    # Act
    file_created = os.path.exists(expected_filename)

    # Assert
    assert file_created, f"Expected file {expected_filename} not found."

# Ticket6b: The file is recreated on each execution.
def test_filecreated_each_execution():

    # Arrange
    filename = "clean_results.csv"
    if os.path.exists(filename): # Delete the file if it exists from previous tests.
        os.remove(filename)
    
    # Act

        # Run script which should create the 'clean_results.csv" file.
    subprocess.run(["python", r'C:\Users\P10364687\OneDrive\Desktop\Professional Development\Advanced Data Fellowship - Level 5\Module 3 - DevOps Engineering\Assessment 2\multiverse-devops-assessment-2\extract/__init__.py'])

    # Assert
    assert os.path.exists(filename)

# Ticket 7: Create an output script
# A new output script will be created which reads in the clean_results.csv CSV file and outputs the results to the command line, row by row.

# Ticket7a: The script uses the existing sub-module to read the CSV file.
def test_existing_submodule_used():
                    
    # Arrange
    filename = "test_file.csv"
    expected_rows = 17

        # Create test CSV file with some data.
    with open(filename, 'w') as f:
        f.write("header1 header2\n")
        for i in range(expected_rows):
            f.write(f"value{i+1}, value{i+1}\n")
    
    # Act
        # Run script which should use the module to read CSV file.
    os.system("python __init__.py -- clean_results.csv test_file.csv")

        # Read the output file generated by the script.
    with open("clean_results.csv", 'r') as f:
        rows = len(f.readlines()) - 1 # Subtract 1 for the header row.

    # Assert
    assert rows == expected_rows

    os.remove(filename) # Remove "test_file.csv" to prevent build-up of redundant files.

# Ticket7b: The printed output will contain all row data and an appropriate header.
def test_row_data_and_headers():

    file_path = 'clean_results.csv'

    def read_csv(file_path):
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            rows = []
            for row in reader:
                rows.append(row)
            return rows
        
    def print_csv(file_path):
        rows = read_csv(file_path)
        headers = rows[0].key()
        print(headers)
        for row in rows:
            print(row.values())

    def test_print_csv():
        # Arrange
        expected_output = []
        with open('clean_results.csv', 'r') as file:
            reader = csv.render(file)
            for row in reader:
                expected_output.append(row)

        # Act
        with captured_output() as (out, err):
            print_csv('clean_results.csv')
        actual_output = out.getvalue().strip().split('\n')
        actual_output = [line.split(',') for line in actual_output]

        # Assert
        assert actual_output == expected_output
