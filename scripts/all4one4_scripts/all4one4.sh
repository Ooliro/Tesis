#!/usr/bin/env sh

# Saca lista de frecuencias de genes mas longitud de secuencias halladas
# PARTE 1: Tabla de HMMER mas base de datos de cromosomas gtf.

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

mkdir resultados;

# Quita encabezados y colas de archivo que empiecen con el caracter "#"
egrep -v "^#" $1 > noheadtail.temp;

# Pasa el archivo a python para reemplazar espacios en blanco por tabuladores
ipython3 whtspc4tabV2.py noheadtail.temp;
rm noheadtail.temp;

# Obtenemos tabbed.tab que usamos para extarer campos específicos
cut -f1,3,4,7,18,19,23- tabbed.tab > dom_fields.temp;
rm tabbed.tab;

# Cortamos campos especificos y descripciones.
cut -f 6- dom_fields.temp | sed 's/\t/ /g' | sed 's/,/ /g' > description.temp;
cut -f -5 dom_fields.temp > data.temp;
paste data.temp description.temp > all_fields.csv;

rm data.temp;
rm description.temp;
rm dom_fields.temp;

# Con el archivo de campos especificos y bien formateado comienza la búsqueda de hits en la base de datos GTF para reescribirlos en el orden original de la tabla HMMER
echo "El archivo all_fields.csv será tu Checkpoint 1, guardalo bien!";
echo "
Comienza la búsqueda, esto puede tardar unos minutos...
"
for S in $(cat all_fields.csv | awk '{print $1}');
do
    echo $S;
    grep $S $2 >> gtf_ordered.csv && echo $S >> ok.txt || echo $S >> fail.txt
done

# Con las tablas ordenadas por HMMER y con datos de gtf, quitamos duplicados utilizando el GenID y python

ipython3 unduplicate_freq_count.py gtf_ordered.csv

# y por último sacamos la lista de especies unicas para el arbol de clados

cut -f1 frequencies.csv | sort | uniq > spp_freq.txt

echo "
---------------------------
||| Búsqueda finalizada |||
---------------------------

Encontraras tus listas en la carpeta de resultados

"


mv all_fields.csv resultados/;
mv gtf_ordered.csv resultados/;
mv no_duplicates.csv resultados/;
mv frequencies.csv resultados/;
mv ok.txt resultados/;
mv fail.txt resultados/;
