#!/usr/bin/env python
# coding: utf-8

"""No_duplicates (Feene3) debe quitar los resultados repetidos"""

import pandas as pd
import sys 

archivo = sys.argv[1]
data = pd.read_table(archivo, header = None)
#data = pd.read_table("/home/raulrosas/Documentos/IFC/lab/eden/scf_ops/resultados/gtf_ordered.csv", header=None)
#print(data.head(n=10))

# Esta parte es para normalizar la columna de taxID a int64 porque por alguna razón los manejaba como float
data.iloc[:,4]=data.iloc[:,4].values.astype(int).astype(int)

#Inicio
data_inicial=len(data)
print("Tus resultados iniciales totales son:", data_inicial)

#Objetivo
pure_data = data.drop_duplicates(subset=2,keep='first')

#Final y escritura
pure_data.to_csv('no_duplicates.csv', index=False, header=False, sep='\t')
data_final = len(pure_data)
print("Tus resultados finales son:", data_final)

