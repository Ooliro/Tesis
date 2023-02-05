#!/usr/bin/env sh

# Este script fue inicialmente diseñado para manejar listas de datos de frecuencias de genes y sus datos correspondientes en las listas de genomes_names_ids.txt. Esto con el fin de poder graficar la frecuencia de genes por especie.
# Uso intencionado: bash finderz.sh freq.csv genomes_names_ids.txt; Toma una tabla de frecuencias de genes para buscar coincidencias  en la lista de genes dada para escribir lo encontrado con nombre de organismo y frecuencia hallada.
echo $1;
echo $2;

echo "
Tabla que determina el orden: $1
";
echo "
Tabla de donde sacaremos la información: $2
";

echo "
INFORMACIÓN

Este script busca conicidencias entre las dos tablas dadas y da una tercera lista con orden determinado por la 1a y con información de la 2a
";

# Busqueda y rescate. Dada la lista 1, busca coincidencias en la lista 2 e imprime las mismas.

rm found.temp
rm numbah.temp
rm new_freq.csv

for S in $(cat $1 | awk '{print $2}');
do
    grep -P "\t$S\t" $2 >> found.temp

    #result=$(grep -E "\W$S\W" $2)
    #lineCount=$(grep -E "\W$S\W" $2 | wc -l)
    #if [ $lineCount -eq 1 ]; then
    #    echo $result >> found.temp.temp
    #else
    #    echo "$S ---> "
    #    echo $result
    #fi

done

# Corta las frecuencia de secuencias obtenidas en la lista 1 para despues agregarlas a la tabla de busqueda y rescate.

cut -f2 $1 > numbah.temp;

# Pega las tablas found y numbah

paste found.temp numbah.temp > new_freqs.csv;

rm found.temp
rm numbah.temp
