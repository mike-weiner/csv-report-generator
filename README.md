# csv-report-generator
Generate a new, custom CSV file with data that you select from every row within an existing CSV file. 

## About this Python Script
Do you deal with large CSV files where you often only need certain columns of data for every row within the file? This tool allows you to read in **only** CSV files and select what columns of data you want pulled from the CSV file that will be placed in a new CSV file that will be generated.

## Script Requirements
* Python 3 - The machine on which you intend to use this script will need Python 3 installed. (Any version of Python 3 will work. The latest, stable build is preferred. 
* CSV File - For the program to execute, you will need a CSV file stored on the machine that will run the script. 

## How to Use this Script
1. Open your machine's terminal or command prompt and navigate to the directory where you have stored this script. 
1. Within the directory, place the CSV you would like to pull data from.
1. Run the command `python3 csv_report_builder.py [Filename of Original CSV] [Column Names (Separated By Comma)]`

* Note: `[Filename of Original CSV]` is the full name of a CSV file such as: `trees.csv`
* Note: `[Column Names (Separated By Comma)]` is a list of the column names you would like in your new CSV file (order matters). (i.e. `name,index,date`)

# Example 
For example, assume I have a CSV file titled `trees.csv` in the same directory that I have the `csv_report_builder.py` script in. The `trees.csv` file has the following column names in the header row:

| Index | "Girth (in)"| "Height (ft)" | "Volume(ft^3)" |
| ----- | ----------- | ------------- | -------------- |

I want a new CSV file with the only these columns in this order:

| "Volume(ft^3)" | "Girth (in)" | Index |
| -------------- | ------------ | ----- |

To accomplish this, I would run the command `python3 csv_report_builder.py trees.csv "Volume(ft^3)","Girth (in)",Index`. This will create a new file in the same directory with the specified columns in the specified order.
