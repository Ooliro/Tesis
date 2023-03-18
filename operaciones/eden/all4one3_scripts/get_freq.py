#!/usr/bin/env python3

import sys
import pandas as pd

"""get_freqs debe agregar la columna correspondiente de clado a las especies que encuentre"""

# Rebel1: No Pandas


## Carga archivos desde la linea de comandos
taxfile = sys.argv[1] # Tabla de clados en 2 columnas
countfile = sys.argv[2]  # Tabla de frecuencias con Spp

## Inicia el diccionario y acomoda las columnas
taxdict1 = {}

with open(taxfile) as infile:
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
with countfile as infile:
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

print("[DONE] :D")

# Rebel2: Pandas
