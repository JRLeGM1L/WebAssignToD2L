#!/usr/bin/env python3
"""
This program is designed to create a csv that will be uploaded to D2L
with WebAssign grades. The program requires two csv files, one with the
scores downloaded from Webassign and another with the D2L grades in D2L that will be
updated.
When downloading the D2L file, make sure you have selected the correct WA activities only.
This program works for a specific csv document format, so the moment WA designs a new one,
the program needs to be adjusted, perhaps rewritten.
"""

import pandas as pd
import subprocess
from datetime import date

today = date.today()

# Move the two files downloaded from WebAssign and from D2L to our folder called WebAssignGradesToD2L
# Then rename the files correspondingly
subprocess.run(["$HOME/WebAssignGradesToD2L/move_files.sh"], shell=True)
print("Please wait...moving files from the Downloads folder to our working directory")
subprocess.run(["$HOME/WebAssignGradesToD2L/D2LFiles/rename_files.sh"], shell=True)
print("Please wait...Renaming D2L file")
subprocess.run(["$HOME/WebAssignGradesToD2L/WebAssignFiles/rename_files.sh"], shell=True)
print("Please wait...Renaming WebAssign file")

# Include the files to the project.
WEBASSIGN_FILE = f'WebAssignFiles/{today.strftime("%Y%m%d")}_WebAssignScores.csv'
D2L_FILE = f'D2LFiles/{today.strftime("%Y%m%d")}_D2LScores.csv'

# This line is necessary because the csv downloaded from WA has useless information in the header.
SKIP_LINES_webassign = 4

# Read both csv files.
webassign_download_scores = pd.read_csv(WEBASSIGN_FILE,header=SKIP_LINES_webassign)
D2L_csvdownload = pd.read_csv(D2L_FILE)
# Drop additional rows from the webassign csv that contain garbage. We only want the grades.
WA = webassign_download_scores.drop([0, 2, len(webassign_download_scores) -1])


# Drop the students full name and username, what we need is the NetId under student number.
WA = WA.drop(WA.columns[[0,1,-1]],axis=1)

# Replace all NS and ND with 0. Annoyingly, WA also gives ND (0) and NS (0) scores.
WA = WA.replace(["NS", "ND", "NS (0)", "ND (0)"], 0)


num_of_columns = len(WA.columns)


# Convert all entries in the columns to float, except obviously the student ID column (which is a string)
WA[WA.columns[list(range(1, num_of_columns))]] = WA[WA.columns[list(range(1, num_of_columns))]].astype(float)

# Scale the entries accordingly. WebAssign has different points for each assignment but in D2L
# they are all worth 10 points.
# First select the weights.
# Need two placeholders for the first two columns have no scores no scale.
weights = [0, 0]
for i in range(num_of_columns - 2):
    weights.append(WA[WA.columns[list(range(2, num_of_columns))]].iloc[0][i])


# Now scale the grades in every column
for i in range(2, num_of_columns):
    WA[WA.columns[i]] = WA[WA.columns[i]].apply(lambda x: x * 10 / weights[i])

# Drop the totals column.
WA = WA.drop(WA.columns[1], axis=1, index=None)
# Drop totals and empty row rows
WA = WA.drop([1, 3])

# Need to put an end-of-line indicator
WA = WA.assign(X= '#' * 1)

# Your csv file to be uploaded has to have the names that come from D2L as headers
WA.columns = D2L_csvdownload.columns

# Use the Username column as index. The file will now be ready to be created to D2L's liking.
WA.set_index('Username', inplace=True)

# Create your csv
WA.to_csv(f"Uploadables/Uploadable{date.today()}.csv")
print("Your file was succesfully created. It is in the Uploadables folder.")

# You should have a new cvs with the name 'Uploadable" and the date. Exit code 0
# means program was successful. Exit code 1 means there was an error.