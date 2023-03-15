#!/usr/bin/env sh

# $1 Determina orden: frecuencias
# $2 Imprime los resultados de aqui: tax_clade con clado

for S in $(cat $1 | awk '{print $1,$2}');
do
    grep -P "\t$S\t" $2 >> found.temp

done
