from extract import *

filename = "results.csv" # Select input file, add as 'filename' variable.
data = read_csv_file(filename) # Read the input csv file.

cleanfilename = "clean_results.csv"
clean_data = write_csv_file(cleanfilename, data) # Write and clean data.

read_clean_csv_file(cleanfilename) # Read clean data into app.

format_clean_csv_file(row) # Output clean dataset into clean results file.