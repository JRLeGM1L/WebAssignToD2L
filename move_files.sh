#!/bin/bash

# Define the source and destination directories. 
# If you want to save this project in different directories
# simply modify the paths accordingly.

# If you have not messed up with your computer, by default
# the files downloaded from the internet are saved in the
# ~/Downloads folder. If you have, modify the paths accordingly.


SOURCE_DIR="$HOME/Downloads"
DEST_DIR="$HOME/WebAssignGradesToD2L"
D2L_DIR="$DEST_DIR/D2LFiles"
WA_DIR="$DEST_DIR/WebAssignFiles"

# Create destination directories if they do not exist
mkdir -p "$D2L_DIR"
mkdir -p "$WA_DIR"

# Get the current date
CURRENT_DATE=$(date +"%Y-%m-%d")

# Find the last two modified files in the Downloads folder. Then move
# the files to the corresponding folder. The files that comes from
# D2L start with 'MATH'. If D2L ever changes this, modify line 37 accordingly.
# This step is done with a while-read loop because D2L is VERY ANNOYING
# and names its files with blank spaces. In order to avoid word
# splitting we move the files this way instead than a standard for-loop.

while IFS= read -r FILE; do
    FILES+=("$FILE")
done < <(ls -t "$SOURCE_DIR" | head -n 2)

# Iterate over each file in the array
for FILE in "${FILES[@]}"; do
    if [[ "$FILE" == MATH* ]]; then
        mv "$SOURCE_DIR/$FILE" "$D2L_DIR/"
    else
        mv "$SOURCE_DIR/$FILE" "$WA_DIR/"
    fi
done
