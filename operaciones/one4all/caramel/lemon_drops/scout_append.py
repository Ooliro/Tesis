#!/usr/bin/env python3

# Open file A
with open('fileA.txt', 'r') as fileA:
    # Create a dictionary to store the accession numbers and rows from file A
    a_dict = {}
    # Iterate over each line in file A
    for line in fileA:
        # Split the line into columns
        cols = line.strip().split('\t')
        # Store the row in the dictionary using the accession number as the key
        a_dict[cols[0]] = cols

# Open file B
with open('fileB.txt', 'r') as fileB:
    # Iterate over each line in file B
    for line in fileB:
        # Split the line into columns
        cols = line.strip().split('\t')
        # Check if the accession number is in the dictionary
        if cols[0] in a_dict:
            # Append the numeric value to the end of the corresponding row in file A
            a_dict[cols[0]].append(cols[1])

# Open a new file to write the updated table
with open('updated_fileA.txt', 'w') as outfile:
    # Iterate over the dictionary to write the updated rows to the output file
    for key, row in a_dict.items():
        outfile.write('\t'.join(row) + '\n')
