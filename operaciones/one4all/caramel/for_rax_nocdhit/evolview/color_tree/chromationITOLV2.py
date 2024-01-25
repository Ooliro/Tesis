#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Argumentos
# Primero el archivo uniques que sale de chromationITOLV2.py

# Important imports
import sys

# Input file name
input_file = sys.argv[1]
print("Archivo utilizado:", input_file)

# Output file name
output_file = "ITOL_color_reference.txt"

# Create a dictionary to map values in the second column to the corresponding third column values
# Here we also add the color code for ITOL as needed, in this case for dataser_colorstrip
column_mapping = {
    "Mammalia": "#FF5733",
    "Actinopteri": "#47D147",
    "Amphibia": "#FFC300",
    "Anthozoa": "#33C7FF",
    "Arachnida": "#B266FF",
    "Ascidiacea": "#FF3366",
    "Aves": "#33FF8D",
    "Bivalvia": "#FF8533",
    "Branchiopoda":"#CC33FF",
    "Cephalopoda": "#33FFD6",
    "Ceratodontiformes": "#FF33A6",
    "Chondrichthyes": "#FFD733",
    "Chromadorea": "#33FF4D",
    "Cladistia": "#FF3366",
    "Gastropoda": "#33FFC0",
    "Hexanauplia": "#FF33A6",
    "Hydrozoa": "#FF5733",
    "Hyperoartia": "#33FF4D",
    "Insecta": "#FF8533",
    "Lepidosauria": "#33C7FF",
    "Leptocardii": "#47D147",
    "Malacostraca": "#FFC300",
    "Testudines": "#33FFD6"
    # Add morre if needed
}

#Open the input and output files
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
#    outfile.write(header_groulabel+"\n")
#    outfile.write(header_op+"\n")
    for line in infile:
        # Split the line into columns based on whitespace (adjust as needed)
        columns = line.strip().split()
        
        # Check if there are at least two columns
        if len(columns) >= 2:
            value_in_second_column = columns[1]

            # Lookup the corresponding third column value in the dictionary
            third_column_value = column_mapping.get(value_in_second_column, "")

            # Append the third column value to the line and write it to the output file
            outfile.write(f"{line.strip()}\t{third_column_value}\n")
        else:
            # If there are less than two columns, just write the line as is
            outfile.write(line)

print("Procesado completo. Salida escrita a:", output_file)

#Headers to identify as grouplabel. There's a total of 5 styles, choose whatever
header_identifier="DATASET_COLORSTRIP\nSEPARATOR COMMA\nDATASET_LABEL,Clades\nCOLOR,#FF5733\nDATA\n"

#second_output= "/home/raulrosas/Documentos/IFC/lab/color_tree/cgchm_pretree/second_color_ann.txt"
#second_output = output_dir + "/second_colorann.txt"
second_output = "ITOL_color_dataset.txt"
with open(output_file, "r") as annotation, open(second_output,"w") as second_annotation:
    second_annotation.write(header_identifier)
#    second_annotation.write(header_op+"\n")
    
    for line in annotation:
        columns = line.strip().split()
        if len(columns) >=3:
            col1=columns[0]
            col3=columns[2]
            second_annotation.write(f"{col1},{col3}\n")
            

print("Segundo procesado completo. Salida escrita a:", second_output)
