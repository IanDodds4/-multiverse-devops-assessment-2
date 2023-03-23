# Ian Dodds, Module 3 (DevOps Engineering): Assessment 2
# Last Edit: 

import csv
filename = "results.csv"

def get_input(filename):
    data = []
    with open(filename) as f:
        for line in f.readlines():
            data.append(line.strip().split(','))

# Ticket 2: Remove duplicate entries
# Add functionality to your input script to ignore or remove any duplicate entries
# from the input data.
# Duplicates are based on the User Id field.

#Ticket2a: A final array is created with duplicate entries removed.
#Ticket2b: Where duplicates are found, the first entry is retained.

    with open(filename, 'r') as f_in:
        lines_set = set()

        for line in f_in:
            lines_set.add(line)

    with open(filename, 'w') as f_out:

        for line in lines_set:
            f_out.write(line)

    return data