# Ian Dodds, Module 3 (DevOps Engineering): Assessment 2
# Last Edit: 

# Ticket 1: In your input script, create a function that will read data from a CSV file.
# Objectives:
#   ● The results.csv data file can be successfully processed into an array.
#   ● Each line of the file is read into a new array item.
#   ● The file read method must be in a sub-module.

import csv

filename = "results.csv"

def get_input(filename):
    data = []
    user_ids = set() # keep track of seen user ids
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        for row in csv_reader:
            user_id = row[0]
            
            if user_id not in user_ids: # for each row in the file, check if the user id is already in the 'user_id' variable, if not then add that id.
                data.append(row)
                user_ids.add(user_id)

    return data

file_path = 'results.csv'
data = get_input(file_path)
print(data)