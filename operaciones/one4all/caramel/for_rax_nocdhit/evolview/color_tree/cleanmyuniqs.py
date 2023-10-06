#!/usr/bin/env python
# coding: utf-8

"""Script para reemplazar los múltiples espacios de las tablas resultado de hmmsearch por tabuladores."""


import re
import sys

#infile = input("File's absolute path:") # Pregunta por la ubicación del archivo a convertir
#tab = open(infile, 'r')
#hmm_tab = tab.read()
#tab.close()

file_name = sys.argv[1]
uwu = open(file_name)
data = uwu.read()
uwu.close()


# Reemplaza los espacios simples por tabs.
hmm_tab = re.sub(' +', ' ', data)

final_tab = hmm_tab.replace(' ', '\t')

# Guarda tu archivo exceptuando la primera línea

#output_file_path = "tabbud.txt"
#with open(output_file_path, "w+") as output_file:
#    for line in final_tab.splitlines("\n")[1:]:
#        output_file.write(line)

save_tab = open('tabbud.tab','w+')
save_tab.writelines(final_tab)
save_tab = save_tab.close()

#print("Listo! busca tu nuevo archivo con el nombre de tabbed.tab")

# Guarda esta segunda tabla delimitada por tabs.
