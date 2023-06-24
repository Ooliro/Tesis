#!/usr/bin/env python
# coding: utf-8

# Archivos a usar 

tags = "/home/raul/Documentos/IFC/repo/operaciones/one4all/caramel/for_rax_nocdhit/scfs_pretree/tag.BED"
subdb = "/home/raul/Documentos/IFC/repo/operaciones/one4all/caramel/for_rax_nocdhit/scfs_pretree/subdb.fasta"
clades = "/home/raul/Documentos/IFC/repo/operaciones/one4all/lolipop/freqs/the_clades/scfs_cc.csv"


tags_dict = {}

with open(tags, "r") as file:
    for line in file:
        cod, acc = line.strip().split("\t")
        tags_dict[cod] = acc

#print(my_dict)


subdb_dict = {}

with open(subdb, "r") as file:
    db_acc = ""
    db_spp = ""

    for line in file:
        if line.startswith(">"):
            # Extract accession number from header
            db_acc = line.split(".")[0][1:]

            # Extract species information from header (within square brackets)
            db_spp = line.split("[")[1].split("]")[0]

            # Store the accession number-species pair in the dictionary
            subdb_dict[db_acc] = db_spp

#print(subdb_dict)

## Este diccionario es de 27 cuando debería ser de 340
clades_dict = {}

with open(clades, "r") as file:
    for line in file:
        columns = line.strip().split("\t")
        clade = columns[0]
        spp = columns[1]
        clades_dict[clade] = spp

#print(clades_dict)


# tags_dict - Diccionario de COD:ACC
# subdb_dict - Diccionario de DB_ACC:DB_SPP
# clades_dict - Diccioanrio de CLADE:SPP

annotation_dict = {}
annotation_file = open("annotation_resume.txt", "w")

for acc, cod in tags_dict.items():
    if acc in subdb_dict:
        ass = subdb_dict[acc]
        if ass in clades_dict.values():
            result = clades_dict[db_spp]
            annotation_dict[cod] = result
            annotation_file.write(f"{cod}\t{result}\n")
            
annotation_file.close()
print(annotation_dict)

