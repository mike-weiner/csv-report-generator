# Import Required Modules
import csv
from datetime import datetime
import os
import sys

# Check for Correct Usage of Command Line
if (len(sys.argv) < 3):
    print("Incorrect Usage:")
    print("   argument 1 - name of CSV file to open")
    print("   argument 2 - column names of CSV file to be written to new CSV (spearted by comman, in order)")

# Get Full Path to Current Working Directory
currentWorkingDirectory = os.path.abspath(os.path.dirname(__file__))

# Check that CSV filename specified by user exists
if not (os.path.isfile(currentWorkingDirectory + '/' + sys.argv[1])):
    print("ERROR:")
    print(sys.argv[1] + " does not exist within " + currentWorkingDirectory)
    print("Place the CSV file in this directory and try again.")
    exit()

# Create file[ath for output specified by user
# The name of the file will be identical to the original file with 'output_' and the date the report is being generated ammended to the beginning
name_of_output = "output-" + datetime.today().strftime('%Y-%m-%d') + '-' + sys.argv[1]
complete_name_of_output = currentWorkingDirectory + '/' + name_of_output

# Get the user's list of column names from the CSV file from the command line
user_entry = sys.argv[2]
user_entry_list = user_entry.split(",")

# Create a file with the generated filename
file_output = open(complete_name_of_output, "w")

# Initialize a variable to store the string that is to be written to the new file
string_to_write_to_file = ''

# Open given file
with open(currentWorkingDirectory + '/' + sys.argv[1]) as csv_file:
    csv_file_reader = csv.reader(csv_file)
    data = [row for row in csv_file_reader]

# Create list to store the indexes of the columns the user wants to write into a new CSV file
list_of_user_requested_cols = []

for colName in user_entry_list: # Loop through every column name specified by the user from the command line
    for col, name in enumerate(data[0]): # Loop through the header row in the original CSV file

        # If we find a match of a column name in the original CSV file and a name from the user's command line argument
        # Store the column index where the data is stored in the file
        if colName.strip() == name.replace('"', '').strip():
            list_of_user_requested_cols.append(col)

# For every row in the CSV file, select the columns specificed by the user
for indx_row, row in enumerate(data):
    for indx_col, user_index in enumerate(list_of_user_requested_cols):

        # If this is the last column in the row, don't add a comma at the end
        if indx_col == len(user_entry_list) - 1:
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