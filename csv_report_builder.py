# Import Required Modules
import csv
import os
import tkinter as tk
from datetime import datetime
from tkinter import filedialog
from tkinter import font

# Create GUI window and set window title
builder_win = tk.Tk()
builder_win.title("CSV Report Builder")

# Set minimum window size
builder_win.minsize(200, 200)


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

        # Get the headers in the CSV files to display next to user input field
        header_label = ''

        # Add all of the differnet headers in the CSV file to the label for the user to see
        for index, col in enumerate(data[0]):
            header_label += '[' + str(index) + '] --> ' + col + '\n'

        header_label.strip()

        # Set the text displayed in the label to all of the CSV header columns
        csv_columns_label['text'] = header_label

        # Change the button to allow the user to select an output directory
        select_file_output_path_button['state'] = 'normal'

    
# Create function to allow user to select destination directory
def select_directory():
    # Get current working directory
    current_wording_directory = os.getcwd()

    builder_win.dirpath = filedialog.askdirectory(initialdir = current_wording_directory, 
                                                  title = "Select a Directory")

    if builder_win.dirpath != '':
        # Change the text field for the user to input a list required columns
        user_column_headers['state'] = 'normal'

        # Change the generate report button to normal to allow the user to generate their report
        generate_report_button['state'] = 'normal'


# Create a function to generate a report in the specified directory
def create_report():
    # Create file[ath for output specified by user
    # The name of the file will be identical to the original file with 'output_' and the date the report is being generated ammended to the beginning
    name_of_output = "output_" + str(datetime.now()) + '_' + builder_win.filename
    complete_name_of_output = os.path.join(builder_win.dirpath, name_of_output + '.csv')

    # Get the user's input from the entry box
    user_entry = user_column_headers.get("1.0", "end-1c")

    # Create a file with the generated filename
    file_output = open(complete_name_of_output, "w")
    
    # Initialize a variable to store the string that is to be written to the new file
    string_to_write_to_file = ''

    # Split user entry by comma
    user_entry_list = user_entry.split(',')

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
select_file_path_label = tk.Label(builder_win, text = "1. Selct a CSV File")
select_file_path_label.grid(row = 0, column = 0, columnspan = 2, sticky='nesw', padx = 15)

select_file_path_button = tk.Button(builder_win, text = "Select a CSV File", command = select_file)
select_file_path_button.grid(row = 1, column = 0, columnspan = 2, sticky='nesw', padx = 15)

# Create label and button for selecting output location of report
select_file_output_path_label = tk.Label(builder_win, text = "2. Select an Output Location for Your Report", wraplength = 200)
select_file_output_path_label.grid(row = 2, column = 0, columnspan = 2, sticky='nesw', padx = 15, pady = (15,0))

select_file_output_path_button = tk.Button(builder_win, text = "Select a Directory", command = select_directory, state = "disabled")
select_file_output_path_button.grid(row = 3, column = 0, columnspan = 2, sticky='nesw', padx = 15)

# Create label to display create report
generate_report_label = tk.Label(builder_win, text = "3. Generate a Custom Report. \n Enter the number of each column of data (separted by comma) in the black box below that you would like in your new report. Order matters.", wraplength = 300)
generate_report_label.grid(row = 4, column = 0, columnspan=2, sticky='nesw', padx = 15, pady = (15,15))

# Create label to display CSV file headers
csv_columns_label = tk.Label(builder_win, text="<-- Columns within this CSV File -->\n")
csv_columns_label.grid(row = 5, column = 0, sticky='nesw', padx = 15)

# Create entry to allow for user input for output file
user_column_headers = tk.Text(width = 20, height = 1, borderwidth = 2, relief = "solid", state = "disabled")
user_column_headers.grid(row = 5, column = 1, sticky='nesw', padx = 15)

# Create a button to generate the report
generate_report_button = tk.Button(builder_win, text = "Generate Report", command = create_report, state = "disabled")
generate_report_button.grid(row = 6, column = 0, columnspan = 2, sticky='nesw', padx = 15, pady = (15,0))

# Create a custom font for the 'Close Program' button
close_pro_button_font = font.Font(weight = 'bold')

# Create a button to close the program
close_program_button = tk.Button(builder_win, text = "Close Program", command = quit)
close_program_button['font'] = close_pro_button_font
close_program_button.grid(row = 7, column = 0, columnspan = 2, sticky='nesw', pady = 7.5, padx = 15)

