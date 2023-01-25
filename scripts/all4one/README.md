# Parseador de tablas de HMMER: Miner

## Instrucciones

### En la terminal...

`$ bash all4one.sh file1 file2`

Donde:

- file1: Tabla obtenida directamente de hmmsearch con hits por dominios.
- file2: Base de datos GTF (Metazoa)

### Requisitos

En una carpeta dedicada para este trabajo, debes tener los scripts de python complementarios:

- whspc4tabV2.py
- feene3.py


## Descripción
El script `all4one.sh` necesita de dos argumentos: 

1. Una tabla de resultados con hits por dominios
2. Una base de datos gtf donde va a buscar coincidencias y pasarlas a un nuevo archivo

Lo que hace es:

a) Limpia y formatea las tablas originales para que puedan ser manipuladas más fácilmente.

b) Separa campos de interés y los guarda en un archivo control para su uso futuro.

c) Provee una lista final de los resultados de la tabla original con sus datos gtf sin isoformas (un solo representante por gen) además de dos listas adicionales de "hits & miss".

-  Lista de secuencias halladas en la base de datos GTF
-  Lista de secuencias no halladas en la base de datos de GTF

## Resultados obtenidos

- all_fields.csv - Contiene los campos de interés de la tabla de HMMER, específicamente: 
	+ Número de acceso
	+ Longitud del dominio
	+ Nombre del modelo/objetivo
	+ E-value
	+ Inicio del dominio hallado
	+ Termino del dominio hallado
	+ Nombre de la proteína y especie