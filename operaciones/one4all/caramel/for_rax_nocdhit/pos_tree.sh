#!/usr/bin/env sh

# Ejecuta este script donde tengas el archivo del árbol, los BED correspondientes a las claves que usaste y su sub-base de datos FASTA
# Primer argumento: árbol o alineamiento que usaste para crearlo
# Segundo argumento: archivo con clados elaborado en "lolipop"

for S in $(awk '/^>/ {gsub(/^>/,"",$0); print}' $1);
do
    grep $S tag.BED >> acc_data.temp
done

awk '{print $1}' acc_data.temp | grep -wf - subdb.fasta>> spp_data.temp
#grep -f spp_data.temp $2 >> found.temp
