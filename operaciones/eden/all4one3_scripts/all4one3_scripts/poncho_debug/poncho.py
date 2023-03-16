#!/usr/bin/env python3
#
#

# Sacar el diccionario de clados
taxfile = "tax_clades.tab"

taxdict = {}
with open(taxfile) as infile:
    for line in infile:
        line = line.strip()
        if line == "":
            continue
        taxa, sp = line.split("\t")
        taxdict[sp] = taxa

countfile = "frequencies.csv"

outfilename = "alfonso.txt"
outfile = open(outfilename, "w")

with open(countfile) as infile:
    for line in infile:
        line = line.strip()
        if line == "":
            continue
        data = line.split("\t")
        if len(data) != 3:
            continue
        spp, taxid, count = line.split("\t")
        newline = "\t".join([taxdict[sp], spp, taxid, count]) + "\n"
        outfile.write(newline)

outfile.close()

print("[DONE] :D")
