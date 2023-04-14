#!/usr/bin/env sh

#!/usr/bin/env sh

# Saca lista de frecuencias de genes mas longitud de secuencias halladas
# PARTE 1: Tabla de HMMER mas base de datos de cromosomas gtf.

echo $1;
echo "
Tabla a procesar: $1
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

# Obtenemos tabbed.tab que usamos para extarer campos específicos
cut -f1,3,4,7,18,19,23- tabbed.tab > dom_fields.temp;
rm tabbed.tab;

# Cortamos campos especificos y descripciones.
cut -f 7- dom_fields.temp | sed 's/\t/ /g' | sed 's/,/ /g' > description.temp;
cut -f -6 dom_fields.temp > data.temp;
paste data.temp description.temp > all_fields.csv;

rm data.temp;
rm description.temp;
rm dom_fields.temp;
