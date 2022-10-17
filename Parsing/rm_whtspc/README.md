# Parseo de tablas de resultados de HMMER

## Paso 1 - Nada de encabezados o colas

Quita las primeras 3 líneas de las tablas, así como las últimas 10. Toda línea sin información relevante lleva un "#" al inicio por lo que puedes quitarlas con:

`egrep -v "^#" example.tab > noheadtail_example.tab`

Con estas tablas sin encabezados ni colas corre el script de python para tener tus tablas separadas por tabs y no por espacios. Quedarán de tal manera que coincidan con el índice de columnas dado en el manual de HMMER y que te transcribo aquí mismo en el archivo `Col_index.txt`. Ten en cuenta que el orden cambia dependiendo del argumento de tabla que utilices: por secuencia o por dominio.

## Paso 2 - Corre el script de python en la terminal

...en eso estamos. 