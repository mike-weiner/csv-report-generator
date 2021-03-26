# csv-report-generator
Generate a new, custom CSV file with data that you select from every row within an existing CSV file. 

## About this Python Script
Do you deal with large CSV files where you often only need certain columns of data or maybe you need to quickly reorder certain columns? This tool allows you to read in a CSV file and select what columns of data you want pulled from the CSV file and in what order you want the columns ordered that will be placed in a new CSV file that will be generated.

## Script Requirements
* Python 3 - The machine on which you intend to use this script will need Python 3 installed. (Any version of Python 3 will work. The latest, stable build is preferred.)
* CSV File - For the program to execute, you will need a CSV file stored on the machine in the same directory where this Python script is stored.

## How to Use this Script
1. Open your machine's terminal or command prompt and navigate to the directory where you have stored this script. 
1. Within the directory, place the CSV you would like to pull data from.
1. Run the command `python3 csv_report_builder.py filename colnames`

* Note: `filename` is the full name of a CSV file you placed into the directory where this script is. (i.e.: `trees.csv`)
* Note: `colnames` is a list of the column names you would like in your new CSV file that are separated by commas with each column name wrapped in double quotes `" "`. Order matters. Include no extra spaces. (i.e.: `"name","index","date"`)

# Example 
Assume I have a CSV file titled `trees.csv` in the same directory that I have the `csv_report_builder.py` script. The `trees.csv` file has the following column names in the header row:

| Index | "Girth (in)"| "Height (ft)" | "Volume(ft^3)" |
| ----- | ----------- | ------------- | -------------- |

I want a new CSV file with the only 3 columns from the original file and I want them in a new order:

| "Volume(ft^3)" | "Girth (in)" | Index |
| -------------- | ------------ | ----- |

To accomplish this, I would navigate to the directory where I have both this Python script and my CSV file saved. I would then run the command `python3 csv_report_builder.py trees.csv "Volume(ft^3)","Girth (in)","Index"`. This will create a new CSV file in the same directory with the "Volume(ft^3)", "Girth (in)", and Index columns in that order. The newly created CSV file will be titled `output-YYYY-mm-dd-trees.csv` where `YYYY-mm-dd` will be today's date.
