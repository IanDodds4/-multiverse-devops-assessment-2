# Ian Dodds, Module 3 (DevOps Engineering): Assessment 2
# Last Edit: 

import csv
filename = "results.csv"

def get_input(filename):
    data = []
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data.append(row)

            return data

file_path = 'results.csv'
data = get_input(file_path)
print(data)