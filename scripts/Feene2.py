#!/usr/bin/env python
# coding: utf-8

"""Feene debe quitar los resultados repetidos"""

import pandas as pd
import sys 

# Pregunta por la ubicación del archivo a convertir
infile = input("File's absolute path:")

data = pd.read_table(infile, header=None)
data_inicial=len(data)
print("Tus resultados iniciales totales son:", data_inicial)
pure_data = data.drop_duplicates(subset=1,keep='first')

pure_data.to_csv('feene.csv', index=False, header=False, sep='\t')

data_final = len(pure_data)
print("Tus resultados finales son:", data_final, "Están en el archivo feene.csv dentro de el mismo directorio que este script!")
