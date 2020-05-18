# csv_report_generator
Generate a new, custom CSV file with data that you select from every row within an existing CSV file. 

## About this Python Script
Do you deal with large CSV files where you often only need certain columns of data for every row within the file? This tool allows you to read in **only** CSV files and select what columns of data you want pulled from the CSV file that will be placed in a new CSV file that will be generated.

## Script Requirements
* Python 3 - The machine on which you intend to use this script will need Python 3 installed. (Any version of Python 3 will work. The latest, stable build is preferred. 
* CSV File - For the program to execute, you will need a CSV file stored on the machine that will run the script. 

## How to Use this Script
1. Open your machine's terminal or command prompt and navigate to the directory where you have stored this script. 
1. Within the directory, run the command `python3 -i csv_report_builder.py` **(Note: This will open the script file in interactive mode that will allow the GUI to open.)**
1. Click on the "Select a CSV File" button to open a file picker dialog. Select the CSV that you would like to pull data from.
1. Click on the "Select a Directory" button to open a directory picker dialog. Select a directory where you would like the new CSV file that will be generated to be saved. 
  **(Note: The output file will be named** `output_<todays_date>_<name_of_your_csv_file>` **where <todays_date> is the date that the report is generated in the form of YYYY-MM-DD HH-MM-SS and <name_of_your_csv_file> is the exact file name of the CSV file you read in.)**
1. A list of all of the columns within the CSV file you selected will be displayed under "Columns within CSV File". Click to select or deselect the names of the columns that you would like in the new CSV file that will be generated.
1. Once you have selected the desired columns that will be generated in a new CSV file, click the "Generate Report" button. 
1. Open a file explorer on your machine, navigate to the directory you specified in Step #4 and open the newly generated CSV file. 
1. Click the "Close Program" button to close the GUI and exit the Python script.

## Image Assets
Below is a screenshot of what this script's GUI looks like when selecting columns of data to be included in the new CSV file. 
<p align="center">
  <img width="343" height="748" src="/gui-overview.png">
</p>
