#!/bin/bash

# -----------------------------------------------------------------------------
# File Permission Manager Script
# This script applies execute permissions (+x) to a target file.
# -----------------------------------------------------------------------------

# --- 1. Argument Check ---
TARGET_FILE=$1

# Check if a filename was provided
if [ -z "$TARGET_FILE" ]; then
    echo "Usage: ./make_exec.sh <filename>"
    echo "Example: ./make_exec.sh my_new_script.sh"
    exit 1
fi

# --- 2. Existence Check ---
# Check if the file actually exists (-f checks for a regular file)
if [ ! -f "$TARGET_FILE" ]; then
    echo "Error: File '$TARGET_FILE' not found."
    exit 1
fi

# --- 3. Apply Execute Permission ---
# Use the 'chmod' command to add the execute permission for the owner, group, and others.
echo "Attempting to set execute permissions for '$TARGET_FILE'..."

# The core command: adds (+) execute (x) permission
chmod +x "$TARGET_FILE"

# --- 4. Verification and Feedback ---
if [ $? -eq 0 ]; then
    echo "Success: Execute permission added."
    echo "New permissions for '$TARGET_FILE':"
    # Display the new permissions string
    ls -l "$TARGET_FILE"
else
    echo "Error: Failed to change permissions. Check your user rights."
fi