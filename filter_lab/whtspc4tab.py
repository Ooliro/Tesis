#!/usr/bin/env python
# coding: utf-8

# Script para reemplazar los múltiples espacios de las tablas resultado de hmmsearch por tabuladores.
# Esto es para hacer más fácil el parseo de datos.
# Dispoible en: https://github.com/Ooliro/Tesis/tree/main/Parsing/rm_whtspc


# Abre el archivo limpio de encabezados y colas innecesarios. 
# Todos los archivos de salida de HMMER tienen "#" al inicio así que purga esos.

import re
import sys

infile = input("File's absolute path:") # Pregunta por la ubicación del archivo a convertir
tab = open(infile, 'r')
hmm_tab = tab.read()
tab.close()

hmm_tab = re.sub(' +', ' ',hmm_tab)

final_tab = hmm_tab.replace(' ', '\t')

# Reemplaza los espacios simples por tabs.

save_tab = open('tabbed.tab','w+')

save_tab.writelines(final_tab)

save_tab = save_tab.close()

print("Done! Your tabbed.tab file is on the same directory as this python script")

# Guarda esta segunda tabla delimitada por tabs.
