#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Enter this as well while executing the pyhton script: pre_annotation file (itool_annotation.txt)

# Important imports
#import sys
#from pathlib import Path

# Input file name
#input_file = sys.argv[1]
input_file = "/home/raul/Documentos/IFC/repo/operaciones/one4all/caramel/for_rax_nocdhit/evolview/color_tree/cgchm_pretree/itool_annotation.txt"
print("Archivo utilizado:", input_file)
# Output file name
output_file = "ITOL_color_ann.txt"

# Create a dictionary to map values in the second column to the corresponding third column values
# Here we also add the color code for ITOL as needed
column_mapping = {
    "Mammalia": "label_background,#FF5733",
    "Actinopteri": "label_background,#47D147",
    "Amphibia": "label_background,#FFC300",
    "Anthozoa": "label_background,#33C7FF",
    "Arachnida": "label_background,#B266FF",
    "Ascidiacea": "label_background,#FF3366",
    "Aves": "label_background,#33FF8D",
    "Bivalvia": "label_background,#FF8533",
    "Branchiopoda":"label_background,#CC33FF",
    "Cephalopoda": "label_background,#33FFD6",
    "Ceratodontiformes": "label_background,#FF33A6",
    "Chondrichthyes": "label_background,#FFD733",
    "Chromadorea": "label_background,#33FF4D",
    "Cladistia": "label_background,#FF3366",
    "Gastropoda": "label_background,#33FFC0",
    "Hexanauplia": "label_background,#FF33A6",
    "Hydrozoa": "label_background,#FF5733",
    "Hyperoartia": "label_background,#33FF4D",
    "Insecta": "label_background,#FF8533",
    "Lepidosauria": "label_background,#33C7FF",
    "Leptocardii": "label_background,#47D147",
    "Malacostraca": "label_background,#FFC300",
    "Testudines": "label_background,#33FFD6"
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
header_identifier="TREE_COLORS\nSEPARATOR COMMA\nDATA\n"
#header_op="SEPARATOR TAB"

#second_output= "/home/raulrosas/Documentos/IFC/lab/color_tree/cgchm_pretree/second_color_ann.txt"
#second_output = output_dir + "/second_colorann.txt"
second_output = "second_colorann.txt"
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
