# Import Required Modules
import csv
import os
import tkinter as tk
from datetime import datetime
from tkinter import filedialog
from tkinter import font
from tkinter import *

# Create GUI window and set window title
builder_win = tk.Tk()
builder_win.title("CSV Report Builder")

# Set minimum window size
builder_win.minsize(200, 400)

# Create function to allow user to select file
def select_file():
    # Get current working directory
    current_wording_directory = os.getcwd()

    builder_win.filepath = filedialog.askopenfilename(initialdir = current_wording_directory, 
                                                      title = "Select CSV File", 
                                                      filetypes = (("CSV Files","*.csv"),))
    
    # Check to make sure that the user has actually selected a CSV file
    if builder_win.filepath != '':
        # Get the filename that is being opened without the file extensions
        builder_win.filename = builder_win.filepath.split('/')
        builder_win.filename = builder_win.filename[-1].split('.')[0]

        # Open given file
        with open(builder_win.filepath) as csv_file:
            csv_file_reader = csv.reader(csv_file)
            data = [row for row in csv_file_reader]

        # Clear Any Items from List Box
        csv_col_select_listbox.delete(0, END)

        # Add all of the differnet headers in the CSV file to the label for the user to see
        for index, col in enumerate(data[0]):
            csv_col_select_listbox.insert(index, col)

        # Change the button to allow the user to select an output directory
        select_file_output_path_button['state'] = 'normal'
    
# Create function to allow user to select destination directory
def select_directory():
    # Get current working directory
    current_wording_directory = os.getcwd()

    builder_win.dirpath = filedialog.askdirectory(initialdir = current_wording_directory, 
                                                  title = "Select a Directory")

    if builder_win.dirpath != '':
        # Change the generate report button to normal to allow the user to generate their report
        generate_report_button['state'] = 'normal'

# Create a function to generate a report in the specified directory
def create_report():
    # Create file[ath for output specified by user
    # The name of the file will be identical to the original file with 'output_' and the date the report is being generated ammended to the beginning
    name_of_output = "output_" + str(datetime.now()) + '_' + builder_win.filename
    complete_name_of_output = os.path.join(builder_win.dirpath, name_of_output + '.csv')

    # Get the user's selection(s) from the Listbox
    user_entry = csv_col_select_listbox.curselection()

    # Create a file with the generated filename
    file_output = open(complete_name_of_output, "w")
    
    # Initialize a variable to store the string that is to be written to the new file
    string_to_write_to_file = ''

    # Convert tuple of user selections from tuple into list
    user_entry_list = list(user_entry)

    # Open given file
    with open(builder_win.filepath) as csv_file:
        csv_file_reader = csv.reader(csv_file)
        data = [row for row in csv_file_reader]

    # For every row in the CSV file, select the columns specificed by the user
    for indx_row, row in enumerate(data):
        for indx_col, user_index in enumerate(user_entry_list):

            # If this is the last column in the row, don't add a comma at the end
            if indx_col == len(user_entry_list) - 1:
                string_to_write_to_file += row[int(user_index)]
            else:
                string_to_write_to_file += row[int(user_index)] + ','

        # If this is the last row in the CSV file, don't add a new line
        if indx_row != len(data) - 1:
            string_to_write_to_file += '\n'
        
    # Strip any additional newline characters from the output file
    string_to_write_to_file.strip()

    # Write the string to the output file and close it
    file_output.write(string_to_write_to_file)
    file_output.close()

# Create label and button for selecting a CSV file
select_file_path_label = tk.Label(builder_win, text = "1. Select a CSV File", bg="#5a5a5a", fg="#ffffff", font="-weight bold", padx = 15)
select_file_path_label.grid(row = 0, column = 0, columnspan = 2, sticky='nesw')

select_file_path_button = tk.Button(builder_win, text = "Select a CSV File", command = select_file)
select_file_path_button.grid(row = 1, column = 0, columnspan = 2, sticky='nesw', padx = 15)

# Create label and button for selecting output location of report
select_file_output_path_label = tk.Label(builder_win, text = "2. Select Save Location", bg="#5a5a5a", fg="#ffffff", font="-weight bold", padx = 15)
select_file_output_path_label.grid(row = 2, column = 0, columnspan = 2, sticky='nesw', pady = (15,0))

select_file_output_path_button = tk.Button(builder_win, text = "Select a Directory", command = select_directory, state = "disabled")
select_file_output_path_button.grid(row = 3, column = 0, columnspan = 2, sticky='nesw', padx = 15)

# Create label for selecting desired column section
generate_report_label = tk.Label(builder_win, text = "3. Select Desired Columns", bg="#5a5a5a", fg="#ffffff", font="-weight bold", padx = 15)
generate_report_label.grid(row = 4, column = 0, columnspan=2, sticky='nesw', pady = (15,0))

# Create label to display CSV headers
csv_columns_label = tk.Label(builder_win, text="Columns within CSV File", font="-weight bold", padx = 15)
csv_columns_label.grid(row = 5, column = 0, columnspan = 2, sticky='nesw', pady = (15,0))

# Create label to instruct users about how to select CSV headers
csv_columns_label = tk.Label(builder_win, text="Select/deselect CSV columns to include in the new report by clicking on the titles below. Click the `Generate Report` button below to create the new CSV file with the selected columns.", wraplength = 200, padx = 15)
csv_columns_label.grid(row = 6, column = 0, columnspan = 2, sticky='nesw', pady = (0, 10))

# Establish Listbox to allow user to select desired CSV columns for output report
csv_col_select_listbox = Listbox(builder_win, selectmode = MULTIPLE, exportselection = 0)
csv_col_select_listbox.grid(row = 7, column = 0, sticky='nesw', padx = (25,0), pady = (0,0))

# Establish Scroll Bar to allow user to Scroll Through List of CSV Column Headers
csv_col_select_scrollbar = Scrollbar(builder_win)
csv_col_select_scrollbar.grid(row = 7, column = 1, sticky='ns', padx = (0,10))

# Link Scroll Bar to List Box for CSV Columns
csv_col_select_listbox.config(yscrollcommand = csv_col_select_scrollbar.set)
csv_col_select_scrollbar.config(command = csv_col_select_listbox.yview)

# Create label for generating report section
generate_report_label = tk.Label(builder_win, text = "4. Generate New CSV", bg="#5a5a5a", fg="#ffffff", font="-weight bold", padx = 15)
generate_report_label.grid(row = 8, column = 0, columnspan=2, sticky='nesw', pady = (15,0))

# Create a button to generate the report
generate_report_button = tk.Button(builder_win, text = "Generate Report", command = create_report, state = "disabled")
generate_report_button.grid(row = 9, column = 0, columnspan = 2, sticky='nesw', padx = 15)

# Create a button to close the program
close_program_button = tk.Button(builder_win, text = "Close Program", command = quit, font="-weight bold")
close_program_button.grid(row = 10, column = 0, columnspan = 2, sticky='nesw', pady = 7.5, padx = 15)