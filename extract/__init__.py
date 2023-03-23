# Ian Dodds, Module 3 (DevOps Engineering): Assessment 2
# Last Edit: 

# Ticket 1: In your input script, create a function that will read data from a CSV file.
# Objectives:
#   ● The results.csv data file can be successfully processed into an array.
#   ● Each line of the file is read into a new array item.
#   ● The file read method must be in a sub-module.

# Ticket 2: Add functionality to your input script to ignore or remove any duplicate entries from the input data. Duplicates are based on the User Id field.
# Objectives:
#   ● A final array is created with duplicate entries removed.
#   ● Where duplicates are found, the first entry is retained.

# Ticket 3: Description Update your input script to ignore any empty lines found when reading in the input data file.
# Objectives 
#   ● A final array is created with any empty lines omitted.

import csv

def get_input(file_path):
    data = []
    user_ids = set() # keep track of seen user ids.
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if not row[0]:
                continue # Ticket 3: Skip empty lines.
            user_id = row[0] # Ticket 2: Track user_ids found, begin creating list.
            if user_id not in user_ids: # Ticket 2: For each row in the file, check if the user id is already in the 'user_id' variable, if not then add that id.
                data.append(row)
                user_ids.add(user_id)
    return data


file_path = 'results.csv'
data = get_input(file_path)
print(data)