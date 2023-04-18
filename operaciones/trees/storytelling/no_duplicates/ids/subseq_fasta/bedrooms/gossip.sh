#!/usr/bin/env sh

# Busqueda y rescate. Dada la lista 1, busca coincidencias en la lista 2 e imprime las mismas.

#Primero ids y luego los campos

for S in $(cat $1 | awk '{print $1}');
do
	echo $S
	grep $S $2 >> catched.temp && echo $S >> found.temp || echo $S >> lost.temp
done

# Con las coincidencias, usa solo el primer campo de números de acceso para eliminar duplicados
sort -u -k1,1 catched.temp > catch_sort.temp

# Y corta solo las columnas de número de acceso, inicio y fin de dominio
cut -f1,5,6 catch_sort.txt > ranges.bed

rm catched.temp
rm found.temp
rm lost.temp
rm catch_sort.temp
