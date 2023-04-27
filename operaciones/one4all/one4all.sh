#!/usr/bin/env sh

# -----|Butterscotch|-----

# -|LOKI|- Obtén tablas listas para manipular

echo $1;
echo $2;
echo "
Tabla de hmmsearch a procesar: $1
";
echo "
Base de datos GTF: $2
";
echo "
¡NOTA IMPORTANTE!

Este script esta diseñado para trabajar con tablas de hits (--domtblout) por dominio de HMMER!
";

# Quita encabezados y colas de archivo que empiecen con el caracter "#"
egrep -v "^#" $1 > noheadtail.temp;

# Pasa el archivo a python para reemplazar espacios en blanco por tabuladores
ipython3 whtspc4tabV2.py noheadtail.temp;
rm noheadtail.temp;

# Lista control de campos
mv tabbed.tab raw_fields.temp;
cut -f1-22 raw_fields.temp > data.temp;
cut -f23- raw_fields.temp |  sed 's/\t/ /g' | sed 's/,/ /g' > description.temp;
paste data.temp description.temp > all_fields.tab;

# Sacamos campos de interés, 11/23 en específico.
cut -f1,3,4,7,16-21,23 all_fields.tab > dom_fields.tab;

# Borramos intermedios
rm data.temp;
rm description.temp;
rm raw_fields.temp

mkdir resultados;
mkdir resultados/control_lists;

# -|YAMATO|- Filtrado a nivel E-value y GeneID

# E-values: Solo los resultados con un e-value mayor o igual a 0.0001 se conservan
awk '$4 <= 0.0001' dom_fields.tab > good_evalues.tab

# De los dominios, toma solo al primero. Esto solo se hace tomando el primer resultado.
awk '!a[$1]++' good_evalues.tab > firstdom_only.tab

#GeneID: Toma como llave la clave de acceso de dom_fields para buscar su homonimo en la base GTF, la imprime y la filtra por duplicados utilizando el GenID
echo "El archivo all_fields.tab será tu Checkpoint 1, guardalo bien!";
echo "
Comienza la búsqueda, esto puede tardar unos minutos...
"
for S in $(cat dom_fields.tab | awk '{print $1}');
do
    echo $S;
    grep $S $2 >> gtf_ordered.csv && echo $S >> gtf_found.txt || echo $S >> gtf_notfound.txt
done

ipython3 unduplicate_freq_count.py gtf_ordered.csv

# Cortamos especies para clados [Lolipop]
cut -f1 frequencies.csv | sort > spp.txt

echo "
---------------------------
||| Búsqueda finalizada |||
---------------------------

Encontraras tus listas en la carpeta de resultados

"

mv spp.txt resultados/;
mv good_evalues.tab resultados/;
mv dom_fields.tab resultados/;
mv gtf_ordered.csv resultados/;
mv no_duplicates.csv resultados/;
mv frequencies.csv resultados/;
mv firstdom_only.tab resultados/;

# Acomodamos controles
mv all_fields.tab resultados/control_lists;
mv gtf_found.txt resultados/control_lists;
mv gtf_notfound.txt resultados/control_lists;
