# Author: Ian Dodds, Module 3 (DevOps Engineering): Assessment 2
# Last Edit: 24/03/2023 [Ian Dodds]

# Ticket 1: In your input script, create a function that will read data from a CSV file.
# Date update added: 23/03/2023 [Ian Dodds]
# Objectives:
#   ● The results.csv data file can be successfully processed into an array.
#   ● Each line of the file is read into a new array item.
#   ● The file read method must be in a sub-module.

# Ticket 2: Add functionality to your input script to ignore or remove any duplicate entries from the input data. Duplicates are based on the User Id field.
# Date update added: 23/03/2023 [Ian Dodds]
# Objectives:
#   ● A final array is created with duplicate entries removed.
#   ● Where duplicates are found, the first entry is retained.

# Ticket 3: Update your input script to ignore any empty lines found when reading in the input data file.
# Date update added: 23/03/2023 [Ian Dodds]
# Objectives 
#   ● A final array is created with any empty lines omitted.

# Ticket 4: Add functionality to your input script to automatically capitalise the first_name and last_name fields found in the input data.
# Date update added: 23/03/2023 [Ian Dodds]
# Objectives 
#   ● All names are capitalised in all data entries.

# Ticket 5: Update your input script to validate the responses to the third answer field. This answer must have a numeric value between 1 and 10.
# Date update added: 23/03/2023 [Ian Dodds]
# Any rows with an invalid value are ignored.
# Objectives 
#   ● A final array is created with the input data excluding any rows where answer 3 is invalid.
#   ● No answer 3 values will be outside the range of 1 to 10.

import csv

def read_csv_file(file_path):

    data = []
    user_ids = set() # Ticket 2: Keep track of seen user ids.

    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file) # Ticket 1: Read data from the csv file.

        for row in csv_reader:

            if not row[0]:
                continue # Ticket 3: Skip empty lines.
            user_id, first_name, last_name, answer_1, answer_2, answer_3 = row[:6]
            first_name = first_name.strip().capitalize() # Ticket 4: Capitalise first name entry
            last_name = last_name.strip().capitalize() # Ticket 4: Capitalise last name entry

            try:
                    answer3 = int(answer_3)
            except ValueError: # Ticket 4: Exclude any invalid answer_3 answers. Ensuring interger values only.
                    continue

            if user_id not in user_ids and 1 <= answer3 <= 10: 
                # Ticket 2: For each row in the file, check if the user id is already in the 'user_id' variable, if not then add that id.
                # Ticket 4: For each row in the file, ensure answer_3 is both greater than or equal to 10 AND less than or equal to 10.
                data.append([user_id, first_name, last_name, answer_1, answer_2, answer_3])
                user_ids.add(user_id)

    return data

# Ticket 6: Add functionality to your input script to output the cleansed data to a new CSV file..
# Date update added: 24/03/2023 [Ian Dodds]
# Objectives:
#   ● A new file is created called clean_results.csv.
#   ● The file is recreated on each execution.
#   ● No invalid or unformatted data is present in the new file

def write_csv_file(file_path, data):
    with open(file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['user_id', 'first_name', 'last_name', 'answer_1', 'answer_2', 'answer_3'])
        for row in data:
            csv_writer.writerow(row)

file_path = 'results.csv'
clean_data = read_csv_file(file_path)
write_csv_file('clean_results.csv', clean_data)

# Ticket 7: A new output script will be created which reads in the clean_results.csv CSV file and outputs the results to the command line, row by row.
# Date update added: 24/03/2023 [Ian Dodds]
# Objectives:
#   ● The script uses the existing sub-module to read the CSV file.
#   ● The printed output will contain all row data and an appropriate header.

def read_clean_csv_file(file_path):
    data = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data

#   ● Stretch: The printed output will be formatted with fixed length strings

def format_clean_csv_file(row):
    # Ticket 7: Defining the fixed-length string format
    id_format = '{:<10}'
    first_name_format = '{:<30}'
    last_name_format = '{:<30}'
    answer_1_format = '{:<15}'
    answer_1_format = '{:<15}'
    answer_1_format = '{:<15}'

    # Ticket 7: Formatting each column with the defined string
    formatted_row = id_format.format(row[0]) + first_name_format.format(row[1]) + last_name_format.format(row[2]) + \
        answer_1_format.format(row[3]) + answer_1_format.format(row[4]) + answer_1_format.format(row[5])

    return formatted_row

file_path = 'clean_results.csv'
clean_data = read_clean_csv_file(file_path)

# Ticket 7: Reads in the clean_results.csv CSV file and outputs the results to the command line, row by row.
for row in clean_data:
     formatted_row = format_clean_csv_file(row)
     print(formatted_row)

