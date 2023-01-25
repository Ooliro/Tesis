#!/usr/bin/env sh

# Inicializando con archivos de HMMER para quitar encabezados y colas.

echo $1;
echo $2;
echo "
Tabla a procesar: $1
";
echo "
Base de datos GTF: $2
";
echo "
¡NOTA IMPORTANTE!

Este script esta diseñado para trabajar con tablas de hits (--domtblout) por dominio de HMMER!
";

egrep -v "^#" $1 > noheadtail.temp;


# Comunicado a python para reemplazar espacios en blanco por tabuladores

ipython3 whtspc4tabV2.py noheadtail.temp;
rm noheadtail.temp;

# Aqui tenemos ya a tabbed.tab para sacar campos específicos

cut -f1,3,4,7,18,19,23- tabbed.tab > dom_fields.temp;
rm tabbed.tab;

cut -f 6- dom_fields.temp | sed 's/\t/ /g' | sed 's/,/ /g' > description.temp;
cut -f -5 dom_fields.temp > data.temp;
paste data.temp description.temp > all_fields.csv;

rm data.temp;
rm description.temp;
rm dom_fields.temp;

echo "El archivo all_fields.csv será tu Checkpoint 1, guardalo bien!";
echo "
Comienza la búsqueda, esto puede tardar unos minutos...
"
# Con SEFI (all_fields.csv) ordenaremos el archivo de gtf's de acuerdo con las tablas de hmmer.

for S in $(cat all_fields.csv | awk '{print $1}');
do
    echo $S;
    grep $S $2 >> gtf_ordered.csv && echo $S >> ok.txt || echo $S >> fail.txt
done

# Con las tablas ordenadas por HMMER y con datos de gtf, necesitamos remover resultados duplicados utilizando el GenID

ipython feene3.py gtf_ordered.csv

echo "
Búsqueda finalizada

Encontraras tus resultados en la tabla no_duplicates.csv

"
