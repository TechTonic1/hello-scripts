#!/bin/bash

# Script to update file permissions
FILE_PATH=$1  # Take file path as a parameter
PERMISSIONS=$2  # Take permission as a parameter

# Check if file exists
if [ -f "$FILE_PATH" ]; then
    # Change permissions of the file
    chmod "$PERMISSIONS" "$FILE_PATH"
    echo "Permissions for $FILE_PATH have been updated to $PERMISSIONS."
else
    echo "File $FILE_PATH does not exist."
fi

