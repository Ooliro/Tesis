#!/usr/bin/env python
# coding: utf-8

"""This scritp extracts the paths from the leaves to the root in a ncbi taxonomy tree, narrow it to spp and clade, and finally append the clade column to an existing table"""

# Argumentos de terminal:
#arg1 = Arbol en formato phylip
#arg2 = Archivo de frecuencias al que se le va a anexar la columna de clados

# Primera parte: Corta hojas y raices
from Bio import Phylo
import sys

# Read files from bash
arbol = open(sys.argv[1])

# read tree
tree = Phylo.read(arbol, 'newick')
tree.ladderize()

# get leaves
leaves = tree.get_terminals()

# get paths
paths = []
for leaf in leaves:
    path = tree.get_path(leaf)
    paths.append(path)

# write to a file
outfile_name = 'branch_leaf.txt'
with open(outfile_name, 'w') as outf:
    for path in paths:
        names = [clade.name for clade in path]
        line = '\t'.join(names) + '\n'
        outf.write(line)

# Segunda parte: Limpia ramas para quedarte con clados y spp
import pandas
archivo=open('branch_leaf.txt')
myclades = []
for line in archivo:
    line = line.split("\t")
    if len(line) == 2:
        myclades.append((line[0], line[1]))
    else:
        myclades.append((line[1], line[-1]))

save_file = open('tax_clades.tab', 'w+')

for elemento in myclades:
    linea = elemento[0] + "\t" + elemento[1]
    save_file.write(linea)
save_file.close()

# Tercera parte: agrega la columa de clados al final de tu archivo objetivo

# Carga archivos desde la linea de comandos
countfile = sys.argv[2]  # Tabla de frecuencias con Spp

## Inicia el diccionario y acomoda las columnas
taxdict1 = {}

with open('tax_clades.tab') as infile:
    for line in infile:
        line = line.strip()
        if line == "":
            continue
        clade, spp = line.split("\t")
        taxdict1[spp] = clade

## Prepara los archivos de salida

outfilename = "clades_n_freqs.tab"
outfile = open(outfilename, "w")

## Con el diccionario, busca coincidencias dentro del archivo de frecuencias y agrega el clado al final
with open(countfile) as infile:
    for line in infile:
        line = line.strip()
        if line == "":
            continue
        data = line.split("\t")
        if len(data) != 3:
            continue
        spp, taxid, freq = line.split("\t")
        newline = "\t".join([taxdict1[spp], spp, taxid, freq]) + "\n"
        outfile.write(newline)

outfile.close()

print("Listo!")
