# Parseo de tablas de resultados de HMMER

## Paso 1 - Nada de encabezados o colas

Quita las primeras 3 líneas de las tablas, así como las últimas 10. Toda línea sin información relevante lleva un "#" al inicio por lo que puedes quitarlas con:

`egrep -v "^#" example.tab > noheadtail_example.tab`

Con estas tablas sin encabezados ni colas corre el script de python para tener tus tablas separadas por tabs y no por espacios. Quedarán de tal manera que coincidan con el índice de columnas dado en el manual de HMMER y que te transcribo aquí mismo en el archivo `Col_index.txt`. Ten en cuenta que el orden cambia dependiendo del argumento de tabla que utilices: por secuencia o por dominio.

## Paso 2 - Corre el script de python en la terminal

Puedes descargar el script de Python 3 "whtspc4tab.py" y ejecutarlo desde tu terminal de Linux de la siguiente manera:

`$ ipython whtspc4tab.py`

Obtendrás esta respuesta:

`File's absolute path:`

Donde debes especificar la ruta donde está guardado tu tabla a trabajar. Por ejemplo:

`/home/usuario/Documentos/tabla_de_hmmer.tab` 

En cuanto le proveas la dirección recibirás un mensaje de confirmación de que tu tabla está lista. La misma se guarda en el mismo directorio donde está el script de python que descargaste. Puedes constatar que la tabla esta separada por tabs y no por espacios con:

`cat --show-tabs tabbed.tab | head`

Y los tabs estarán representados con un `^`.