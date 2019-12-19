# csv_report_generator
Generate a custom CSV file with data that you select from every row within an existing CSV file. 

## About this Python Script
Have you ever had a complex CSV files, but you only wanted certain columns of data from every row within that CSV file? This tool allows you to read in only CSV files and select what columns of data you want pulled from the CSV file that will be placed in a new CSV file that will be generated. **(Note: You can only read in CSV files.)** 

## Script Requirements
* Python 3 - The machine on which you intend to use this script will need Python 3 installed. (Any version of Python 3 will work. The lastest, stable build is prefered. 
* CSV File - For the program to exectue, you will need a CSV file stored on the machine that will run the script. 

## How to Use this Script
1. Open your machine's terminal or command prompt and navigate to the directory where you have stored this script. 
1. Within the directory, run the command `python3 -i csv_report_builder.py` **(Note: This will open the script file in interactive mode that will allow the GUI to open.)**
1. Click on the "Select a CSV File" button to open a file picker dialog. Select the CSV that you would like to pull data from.
1. Click on the "Select a Directory" button to open a directory picker dialog. Select a directory where you would like the new CSV file that will be generated to be saved. 
  **(Note: The output file will be nammed** `output_<todays_date>_<name_of_your_csv_file>` **where <todays_date> is the date that the report is generated in the form of YYYY-MM-DD HH-MM-SS and <name_of_your_csv_file> is the exact file name of the CSV file you read in.)**
1. A list of all of the columns and their index numbers will be displayed under "<-- Columns within this CSV File -->". In the textbox outlined with a black border to the right of this list, enter the index numbers of each column that you would like included in your output file separated by commas. **(Note: You must separate each number by a comma and the order in which you enter the column numbers matters. See the [example scenario](https://github.com/mike-weiner/csv_report_generator/tree/master#exampel-scenario) below. )**
1. Once you have entered the desired data that will be generated in a new CSV file, click the "Generate Report" button. 
1. Open a file explorer on your machine, navigate to the directory you specified in Step #4 and open the newly generated CSV file. 
1. Click the "Close Program" button to close the GUI and exit the Python script.

## Exampel Scenario
If you had a CSV file that had a person's Prefix in index 0 (`[0]`), a person's First Name in index 1 (`[1]`), a person's Middle Name in index 2 (`[2]`), a person's Last Name in index 3 (`[3]`), and their Email Address in index 4 (`[4]`) entering `1,3,4` in the textbox would create a CSV file at the directory your specified with the columns `First Name, Last Name, and Email` (in that order).

Entering `4,3,1` in the textbox would create a CSV file at the directory your specified with the columns `Email, Last Name, First Nmae` (in that order).

Entering `3,2,1` in the textbox would create a CSV file at the directory your specified with the columns `Last Name, Middle Name, First Nmae` (in that order).

Entering `3,1` in the textbox would create a CSV file at the directory your specified with the columns `Last Name, First Nmae` (in that order).

Entering `0, 1` in the textbox would create a CSV file at the directory your specified with the columns `Prefix, First Nmae` (in that order).

As you can see, index numbers can be entered in any order as long as they are separated by a comma. **(Note: Entering anything other than numbers separted by a comma will result in an error.)**

## Common Errors
* Entering anything other than numbers separted by commas in the textbox wtih a black border will result in an error. To fix this, please remove anything other than a combination of numeric values that are listed under `<-- Columns within this CSV File -->` separated by commas. (See the [example scenario](https://github.com/mike-weiner/csv_report_generator/tree/master#exampel-scenario) for further explanation and examples.) 

## Image Assets
Below is a screenshot of that this script's GUI looks like before opening a CSV to read data from. 
![Alt text](screenshot1.png?raw=true "CSV Report Generator GUI")
