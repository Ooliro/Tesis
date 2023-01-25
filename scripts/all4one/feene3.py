#!/usr/bin/env python
# coding: utf-8

"""Feene debe quitar los resultados repetidos"""

import pandas as pd
import sys 

archivo = sys.argv[1]
data = pd.read_table(archivo, header = None)
#rough_data = pd.read_table(data, header=None)

data_inicial=len(data)
print("Tus resultados iniciales totales son:", data_inicial)
pure_data = data.drop_duplicates(subset=2,keep='first')

pure_data.to_csv('no_duplicates.csv', index=False, header=False, sep='\t')

data_final = len(pure_data)
print("Tus resultados finales son:", data_final, "Están en el archivo no_duplicates.csv dentro de eeste mismo directorio!")
