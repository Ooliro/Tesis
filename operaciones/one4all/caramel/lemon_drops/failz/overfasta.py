#!/usr/bin/env python3

fasta_file = 'input.fasta'
new_desc_file = 'new_desc.txt'
output_file = 'output.fasta'

# Load the new descriptions from file into a dictionary
new_desc = {}
with open(new_desc_file, 'r') as f:
    for line in f:
        accession, desc = line.strip().split('\t')
        new_desc[accession] = desc

# Parse the FASTA file and replace the descriptions
with open(output_file, 'w') as out_f:
    with open(fasta_file, 'r') as in_f:
        for line in in_f:
            if line.startswith('>'):
                # Extract the accession number from the description line
                accession = line.strip().lstrip('>')
                # Replace the description line with the new description if a match is found
                if accession in new_desc:
                    out_f.write('>' + accession + ' ' + new_desc[accession] + '\n')
                else:
                    out_f.write(line)
            else:
                out_f.write(line)
