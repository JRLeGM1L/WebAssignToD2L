#!/bin/bash


TARGET_DIR="$HOME/WebAssignGradesToD2L/D2LFiles"

# Get the most recently added file in the directory
LATEST_FILE=$(ls -t "$TARGET_DIR" | head -n 1)

# Get the current date in YYYYMMDD format
CURRENT_DATE=$(date +%Y%m%d)

# Remove white spaces from the file name and add the date
NEW_NAME="${CURRENT_DATE}_D2LScores.csv"

# Rename the file
mv "$TARGET_DIR/$LATEST_FILE" "$TARGET_DIR/$NEW_NAME"