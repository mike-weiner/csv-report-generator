# Import Required Modules
import csv
from datetime import datetime
import os
import sys

# Check for Correct Usage of Command Line
if (len(sys.argv) < 3):
    print("Incorrect Usage:")
    print("   python3 csv_report_builder.py filename colnames")
    print("   filename - name of CSV file to open (i.e.: trees.csv)")
    print("   colnames - column names of CSV file to be written to new CSV (i.e.: name,age,sex)")
    exit()

# CONSTANTS
CURRENTWORKINGDIR = os.path.abspath(os.path.dirname(__file__)) # Get Full Path to Current Working Directory
FILENAME = sys.argv[1] # Get the filename of the CSV that needs to be read from the user's command line argument
COLNAMES = sys.argv[2]

# Check that CSV filename specified by user exists
if not (os.path.isfile(CURRENTWORKINGDIR + '/' + FILENAME)):
    print("ERROR:")
    print(FILENAME + " does not exist within " + CURRENTWORKINGDIR)
    print("Place the CSV file in this directory and try again.")
    exit()

# Create filepath for output specified by user
# The name of the file will be identical to the original file with 'output-YYYY-mm-dd' appended to the beginning of the filename
#   YYYY-mm-dd is the current date 
name_of_output = "output-" + datetime.today().strftime('%Y-%m-%d') + '-' + FILENAME
complete_name_of_output = CURRENTWORKINGDIR + '/' + name_of_output

# Create a file with the generated filename
file_output = open(complete_name_of_output, "w")

# Create a list of column names that need to be pulled out from the original CSV file
list_of_colnames_to_output = COLNAMES.split(",")

# Initialize a variable to store the string that is to be written to the new file
string_to_write_to_file = ''

# Open original CSV file passed in by the user
with open(CURRENTWORKINGDIR + '/' + FILENAME) as csv_file:
    csv_file_reader = csv.reader(csv_file)
    data = [row for row in csv_file_reader]

# Create list to store the indexes of the columns the user wants to write into a new CSV file
list_of_col_indexes_matching_requested_cols = []

for colName in list_of_colnames_to_output: # Loop through every column name specified by the user from the command line
    for col, name in enumerate(data[0]): # Loop through the header row in the original CSV file

        # If we find a match of a column name in the original CSV file and a name from the user's command line argument
        # Store the column index where the data is stored in the file
        if colName.strip() == name.replace('"', '').strip():
            list_of_col_indexes_matching_requested_cols.append(col)

# For every row in the CSV file, select the columns specificed by the user
for indx_row, row in enumerate(data):
    for indx_col, user_index in enumerate(list_of_col_indexes_matching_requested_cols):

        # If this is the last column in the row, don't add a comma at the end
        if indx_col == len(list_of_colnames_to_output) - 1:
            string_to_write_to_file += row[int(user_index)].strip()
        else:
            string_to_write_to_file += row[int(user_index)].strip() + ','

    # If this is the last row in the CSV file, don't add a new line
    if indx_row != len(data) - 1:
        string_to_write_to_file += '\n'
    
# Strip any additional newline characters from the output file
string_to_write_to_file.strip()

# Write the string to the output file and close it
file_output.write(string_to_write_to_file)
file_output.close()