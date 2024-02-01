#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Argumentos
# Primero: El archivo uniques que sale de referenceXuniques.py o el archivo temporal de llamado itol_annotation.txt que salio de pos_tree.py

# Important imports
import sys

# Input file name
input_file = sys.argv[1]
#input_file = "/home/raulrosas/Documentos/IFC/repo/operaciones/one4all/caramel/for_rax_nocdhit/evolview/color_tree/cgchm_pretree/itool_annotation.txt"
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

#Headers to identify as grouplabel. Here we use the headers that correspond to the DATASETS annotation files, be sure to use the correct one for your use

#DATASET_COLORSTRIP STYLE, to add a strip outside the branches
header_identifier="DATASET_COLORSTRIP\nSEPARATOR COMMA\nDATASET_LABEL,Clades\nCOLOR,#FF5733\nDATA\n"

#DATASET_STYLE STYLE (heh), to change color and style of the branch inside the tree
#header_identifier="DATASET_STYLE\nSEPARATOR COMMA\nDATASET_LABEL,CATZ\nCOLOR,#ffff00\nDATA\n"

second_output = "ITOL_color_dataset.txt"
with open(output_file, "r") as annotation, open(second_output,"w") as second_annotation:
    second_annotation.write(header_identifier)
    for line in annotation:
        columns = line.strip().split()
        if len(columns) >=3:
            col1=columns[0]
            col3=columns[2]
            second_annotation.write(f"{col1},{col3}\n")

print("Segundo procesado completo. Salida escrita a:", second_output)


extended_clade_file = "extended_clades.txt" # New file
extended_in_file = "ITOL_color_reference.txt" # Reference file from first mapping

# This is so you can simplify the clades to... simpler clades!
second_column_mapping = {
    "Mammalia": "Chordata",
    "Actinopteri": "Chordata",
    "Amphibia": "Chordata",
    "Anthozoa": "Cnidaria",
    "Arachnida": "Arthropoda",
    "Ascidiacea": "Chordata",
    "Aves": "Chordata",
    "Bivalvia": "Mollusca",
    "Branchiopoda":"Arthropoda",
    "Cephalopoda": "Mollusca",
    "Ceratodontiformes": "Chordata",
    "Chondrichthyes": "Chordata",
    "Chromadorea": "Nematoda",
    "Cladistia": "Chordata",
    "Gastropoda": "Mollusca",
    "Hexanauplia": "Arthropoda",
    "Hydrozoa": "Cnidaria",
    "Hyperoartia": "Chordata",
    "Insecta": "Arthropoda",
    "Lepidosauria": "Chordata",
    "Leptocardii": "Chordata",
    "Malacostraca": "Arthropoda",
    "Testudines": "Chordata"
    # Add more if needed    
}

with open(extended_in_file, "r") as infile, open(extended_clade_file, "w") as outfile:
    for line in infile:
        reference_columns = line.strip().split()
        
        # Check if there are at least three columns
        if len(reference_columns) >= 3:
            clade_in_second_column = reference_columns[1]
            
            # Search for the corresponding extended column value in the dictionary
            extended_column_value = second_column_mapping.get(clade_in_second_column, "")
            
            # Append the extended column value to the line and write it to the output file
            outfile.write(f"{line.strip()}\t{extended_column_value}\n")
        else:
            # If there are less than 3 columns, write the line as is
            outfile.write(line)


simple_output_file = "extended_simple_clades.txt" # New file
long_extended_clades = "extended_clades.txt" # Reference file with 4 columns, from the second mapping

# This is so you can color the simpler clades!
third_column_mapping = {
    "Arthropoda":"#fcba03",
    "Chordata":"#fc2c03",
    "Cnidaria":"#03d7fc",
    "Mollusca":"#017d0e",
    "Nematoda":"#7d0173"
}

with open(long_extended_clades,"r") as infile, open(simple_output_file,"w") as outfile:
    for line in infile:
        simplified_columns = line.strip().split()

        # Check if there are at least 4 columns
        if len(simplified_columns) >= 4:
            clade_in_fourth_column = simplified_columns[3]

            # Search for the corresponding simplified column value in the dictionary
            simplified_column_value = third_column_mapping.get(clade_in_fourth_column,"")

            # Append the extended column value to the line and wirte it to the output file
            outfile.write(f"{line.strip()}\t{simplified_column_value}\n")
        else:
            # If there are less than 4 columns, write the line as is
            outfile.write(line)

# Header for DATASET_COLORSTRIP, outside the branches

ds_colors_header = "DATASET_COLORSTRIP\nSEPARATOR TAB\nDATASET_LABEL\tCLADES\nCOLOR\t#ffff00\nDATA\n"
simplified_output_file = "ITOL_simplified_clades.txt" # New file

with open(simple_output_file, "r") as infile, open(simplified_output_file,"w") as outfile:
    outfile.write(ds_colors_header)
    for line in infile:
        columns = line.strip().split()
        if len(columns) >= 4:
            cod = columns[0]
            color = columns[4]
            sim_clade = columns[3]
            outfile.write(f"{cod}\t{color}\t{sim_clade}\n")

print("Archivos de clados simplificados escrita a:", simplified_output_file)
