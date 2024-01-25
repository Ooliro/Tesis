#!/usr/bin/env python
# coding: utf-8

"""Con este script preparamos un archivo tipo BED que contiene COD:Clado que deberá ser cpnvertido a un archivo de anotación por colores en ITOL"""

# Args
# Primero: archivo uniques.phy que obtenemos de iqtree
# Segundo: archivo que temporalmente llamamos "itol_annotation.txt" que salió de pos_tree

# Important imports
import pandas as pd
import re
import io

# Convertimos el archivo "uniques" a un formato más fácil de trabajar, bajo el mismo principio de whtspc4tab
file_name = sys.argv[1]
#file_name = "/home/beemo/Documentos/repo/operaciones/one4all/caramel/for_rax_nocdhit/iqstuff/cgchm_pretree/cgchm_10gap.fa.uniqueseq.phy"
uwu = open(file_name)
data = uwu.read()
uwu.close()

# Sustituimos espacios multiples espacios en blanco por uno solo y luego por un tabulador
ugly_tab = re.sub(' +', ' ', data)
pretty_tab = ugly_tab.replace(' ', '\t')

# Utilizamos esa variable modificada como archivo a convertir en dataframe con StringIO y lo cargamos a pandas
temp_df=io.StringIO(pretty_tab)
uniques = pd.read_csv(temp_df, skiprows=1, sep="\t", names=["COD","Sequence"] )

# Cargamos la lista de referencia que tiene codigos y clados que pasaron y no pasaron el filtro de iqtree
reference = sys.arg[2]
#reference = pd.read_csv("cgchm_pretree/itool_annotation.txt", sep="\t", names=["COD","Clade"])

# Combina los archivos sólo en los archivos que coincidan en la columna "COD"
merged_df = pd.merge(reference, uniques, on=["COD"], how="inner")

# Guarda el resultado al nuevo archivo "uniques.txt"
merged_df[['COD', 'Clade']].to_csv('uniques.txt', index=False, sep='\t')  # Adjust 'sep' based on your preferred delimiter

# Mensaje de compeltado
print("Archivo de COD y Clados guardado a: 'uniques.txt'")
