#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Argumentos
# Primero: El archivo uniques que sale de referenceXuniques.py o el archivo temporal de llamado itol_annotation.txt que salio de pos_tree.py

# Important imports
import sys
import pandas as pd

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

# Content for the ds_legend_label variable
source_file = "extended_simple_clades.txt"
pd_file = pd.read_csv(source_file, sep = "\t", header = None)
interest_column = pd_file.iloc[:,3]
unique_labels = sorted(interest_column.unique())
result_labels = '\t'.join(unique_labels) # Usable VAR

# Content count for colors, shapes and scales
elements_count = len(unique_labels)

# Content for the ds_legend_colors, assuming the main clades are the one in the third_column_mapping
# Arthtopoda, Chordata, Cnidaria, Mollusca & Nematoda (5 total)
color_mapping = {
    1:["#fcba03"],
    2:["#fcba03","#fc2c03"],
    3:["#fcba03","#fc2c03","#03d7fc"],
    4:["#fcba03","#fc2c03","#03d7fc","#017d0e"],
    5:["#fcba03","#fc2c03","#03d7fc","#017d0e","#7d0173"],
    6:["#fcba03","#fc2c03","#03d7fc","#017d0e","#7d0173", "#0c34fa"],
    7:["#fcba03","#fc2c03","#03d7fc","#017d0e","#7d0173", "#0c34fa","#d60cfa"],
}

label_hex_col = color_mapping.get(elements_count,['#000000']*elements_count)
hex_line = '\t'.join(label_hex_col) # USABLE VAR

# Content for ds_legend_shapes
shape_line = '\t'.join(['1']*elements_count) # USABLE VAR

#Content for ds_legend_shape_scales
scale_line = '\t'.join(['1']*elements_count) # USABLE VAR

# File headers for DATASET_COLORSTRIP format, outside the branches

# First: Obligatory stuff, you HAVE to change the separator according to your data. Then LABEL, COLOR can be whatever you want.
ds_colors_header = "DATASET_COLORSTRIP\nSEPARATOR TAB\nDATASET_LABEL\tCLADES\nCOLOR\t#ffff00\n"

#Second: This will affect the legend atop your tree, particulary it's position and name/title
ds_legend_header = "LEGEND_TITLE\tCOLORED_CLADES\nLEGEND_POSITION_X\t250\nLEGEND_POSITION_Y\t100\nLEGEND_HORIZONTAL\t0\n"

# Third: Shapes for your legend's figures. You can use either one from 1-5, or use just one type, up to you.
ds_legend_shapes = "LEGEND_SHAPES\t"+ shape_line + "\n"

# Fourth: Colors for your legend's figures. This HAVE to match the ones you use in your actual data so it is useful of something
ds_legend_colors = "LEGEND_COLORS\t" + hex_line + "\n"

#Fifth: Labels for your legend's figure. This HAVE to match your actual data so you can tell them apart
ds_legend_lables = "LEGEND_LABELS\t" + result_labels + '\n'

# Sixth: Scale/size of the shapes, keeping it in one is good enough.
ds_legend_shape_scales = "LEGEND_SHAPE_SCALES\t" + scale_line + "\n"

# Final: Delimiter for actual data
ds_data_delimiter_head = "DATA\n"

# Actual DATA writing
simplified_output_file = "ITOL_simplified_clades.txt" # New file

with open(simple_output_file, "r") as infile, open(simplified_output_file,"w") as outfile:
    outfile.write(ds_colors_header)
    outfile.write(ds_legend_header)
    outfile.write(ds_legend_shapes)
    outfile.write(ds_legend_colors)
    outfile.write(ds_legend_lables)
    outfile.write(ds_legend_shape_scales)
    outfile.write(ds_data_delimiter_head)
    for line in infile:
        columns = line.strip().split()
        if len(columns) >= 4:
            cod = columns[0]
            color = columns[4]
            sim_clade = columns[3]
            outfile.write(f"{cod}\t{color}\t{sim_clade}\n")

print("Archivos de clados simplificados escrita a:", simplified_output_file)

# Creating CHN colored datasets

# Chitin
input = "ITOL_color_reference.txt"
color_reference_file = pd.read_csv(input, sep = "\t", header = None)
chitin_search = color_reference_file[color_reference_file[0].str.contains("C")]
chitin_search.to_csv("chitin_list.txt", index = False, sep = "\t", header = ["COD","part_clade","part_color"])
chitin_file = pd.read_csv("chitin_list.txt", sep = "\t")
chitin_file["C_Color"]= "#ff4000" #orange
chitin_file[["COD","C_color"]].to_csv("chitin_coloring.txt", index = False, sep ="\t")
# Hyaluronan
hyl_search = color_reference_file[color_reference_file[0].str.contains("H")]
hyl_search.to_csv("hyl_list.txt", index = False, sep = "\t", header = ["COD","part_clade","part_color"])
hyl_file = pd.read_csv("hyl_list.txt", sep = "\t")
hyl_file["C_Color"]= "#46ff03" #green
hyl_file[["COD","C_color"]].to_csv("hyl_coloring.txt", index = False, sep ="\t")
# Unidentified
unid_search = color_reference_file[color_reference_file[0].str.contains("C")]
unid_search.to_csv("unidentified_list.txt", index = False, sep = "\t", header = ["COD","part_clade","part_color"])
unid_file = pd.read_csv("unidentified_list.txt", sep = "\t")
unid_file["C_Color"]= "#fff203" #yellow
unid_file[["COD","C_color"]].to_csv("unidentified_coloring.txt", index = False, sep ="\t")