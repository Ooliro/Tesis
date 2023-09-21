#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 16:42:05 2023

@author: raulrosas
"""

# Input file name
input_file = "/home/raulrosas/Documentos/IFC/lab/color_tree/cgchm_pretree/itool_annotation.txt"

# Output file name
output_file = "/home/raulrosas/Documentos/IFC/lab/color_tree/cgchm_pretree/color_ann.txt"

# Create a dictionary to map values in the second column to the corresponding third column values
column_mapping = {
    "Mammalia": "bkcolor=#FF5733,text=Mamiferos,fontsize=16",
    "Actinopteri": "bkcolor=#47D147,text=Peces,fontsize=16",
    "Amphibia": "bkcolor=#FFC300,text=Anfibios,fontsize=16",
    "Anthozoa": "bkcolor=#33C7FF,text=Polipos,fontsize=16",
    "Arachnida": "bkcolor=#B266FF,text=Aracnidos,fontsize=16",
    "Ascidiacea": "bkcolor=#FF3366,text=Ascidias,fontsize=16",
    "Aves": "bkcolor=#33FF8D,text=Aves,fontsize=16",
    "Bivalvia": "bkcolor=#FF8533,text=Bivalvos,fontsize=16",
    "Branchiopoda":"bkcolor=#CC33FF,text=Branquiopodos,fontsize=16",
    "Cephalopoda": "bkcolor=#33FFD6,text=Cefalopodos,fontsize=16",
    "Ceratodontiformes": "bkcolor=#FF33A6,text=Ceratodontiformes(Peces),fontsize=16",
    "Chondrichthyes": "bkcolor=#FFD733,text=Cartilaginosos(Peces),fontsize=16",
    "Chromadorea": "bkcolor=#33FF4D,text=Cromadoreos(Nematodos),fontsize=16",
    "Cladistia": "bkcolor=#FF3366,text=Cladistia(Peces_oseos),fontsize=16",
    "Gastropoda": "bkcolor=#33FFC0,text=Gastropodos,fontsize=16",
    "Hexanauplia": "bkcolor=#FF33A6,text=Hexanauplia(Crustaceos),fontsize=16",
    "Hydrozoa": "bkcolor=#FF5733,text=Hydrozoa,fontsize=16",
    "Hyperoartia": "bkcolor=#33FF4D,text=Hyperoartia(Lampreas),fontsize=16",
    "Insecta": "bkcolor=#FF8533,text=Insectos,fontsize=16",
    "Lepidosauria": "bkcolor=#33C7FF,text=Lepidosaurios(Lagartos),fontsize=16",
    "Leptocardii": "bkcolor=#47D147,text=Cefalocordados,fontsize=16",
    "Malacostraca": "bkcolor=#FFC300,text=Malacostraca(Crustaceos),fontsize=16",
    "Testudines": "bkcolor=#33FFD6,text=Testudines(Tortugas),fontsize=16"
    # Add morre if needed
}

# Open the input and output files
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
