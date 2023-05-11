#!/usr/bin/env python3

import pandas as pd

# Read in the two files
df_a = pd.read_csv('fileA.csv')
df_b = pd.read_csv('fileB.csv')

# Merge the two dataframes based on the accession number column
merged_df = pd.merge(df_a, df_b, on='accession_number')

# Prompt the user to choose which file's match line to print
choice = input("Enter 'a' to print match line from file A, 'b' to print match line from file B: ")

# Print the match line from the selected file for each row in the merged dataframe
for index, row in merged_df.iterrows():
    if choice == 'a':
        print(row[df_a.columns])
    elif choice == 'b':
        print(row[df_b.columns])
    else:
        print("Invalid choice. Exiting...")
        break
