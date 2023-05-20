#!/usr/bin/env python3

fasta_file = "scfm-hit.fasta"
mapping_file = "tag.BED"
output_file = "modified.fasta"

# Read the mapping file and create a dictionary of partial names to new names
mapping = {}
with open(mapping_file, "r") as f:
    for line in f:
        partial_name, new_name = line.strip().split("\t")
        mapping[partial_name] = new_name

# Open the input FASTA file and the output file
with open(fasta_file, "r") as f_in, open(output_file, "w") as f_out:
    for line in f_in:
        if line.startswith(">"):
            header = line.strip()[1:]  # Remove the ">" character
            new_header = header
            for partial_name, new_name in mapping.items():
                if partial_name in header:
                    new_header = header.replace(partial_name, new_name)
                    break
            new_header = new_header.split(":")[0]  # Remove second part delimited by ":"
            new_header = new_header.split(".")[0]  # Remove second part delimited by "."
            f_out.write(f">{new_header}\n")
        else:
            f_out.write(line)
