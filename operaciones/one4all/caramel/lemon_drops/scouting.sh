#!/usr/bin/env sh

# Prompt user to choose which file to print the match from
read -p "Print match from file A or B? (A/B) " choice

if [ "$choice" == "A" ]; then
  match_file="fileA.txt"
else
  match_file="fileB.txt"
fi

# Read file A and store accession numbers in an array
declare -A accession_array
while read -r line; do
  accession=$(echo "$line" | awk '{print $1}') # assuming accession number is in first column
  accession_array[$accession]=1
done < "fileA.txt"

# Read file B and print matching lines
while read -r line; do
  accession=$(echo "$line" | awk '{print $1}') # assuming accession number is in first column
  if [ "${accession_array[$accession]}" == "1" ]; then
    if [ "$choice" == "A" ]; then
      echo "$line"
    else
      echo "$match_file $line"
    fi
  fi
done < "fileB.txt"
