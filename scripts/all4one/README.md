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
	
- gtf_ordered.csv - Esencialmente es la lista original de HMMER pero con la información de los gtf. Esta conserva el orden original por lo que puedes usarla sin muchas preocupaciones, pero ten en cuenta que perdemos algunas secuencias (8% aproximadamente) porque por alguna razón desconocida no todas las secuencias del refseq están anotados con gtf.

- no_duplicates.csv - Lista final sin isoformas (filtrado por genID, columna 3) con información de gtf's. Tecnicamente sigue ordenada asi que checala!

### Listas complementarias

- ok.txt - Secuencias halladas en la correlación HMMER/GTF. Esto significa que cada secuencia que aparece en esta lista, tiene anotación dentro de los archivos GTF de Metazoa.

- fail.txt - Secuencias no halladas en la correlación HMMER/GTF. Es decir, el complemento "negativo" donde tenemos a resultados de HMMER sin anotación en archivos GTF de Metazoa.

## Instrucciones para sacar graficas de frecuencias de genes

`finderz.sh` es un script que necesita también de `whtspc4tabV2.py` para modificar la tabla de frecuencias que puedes sacar de tus tablas de `no_suplicates.csv`. Por ahora tienes que hacerlo manualmente porque no lo he agregado al script principal (no se si será de mucha ayuda aún), y se hace así:

cut -f5 no_duplicates.csv | sort | uniq -c | sort -r > freq_hmmmodel.tab

Con eso listo pasamos a la terminal:

`bash finderz.sh freq_hmmmodel.tab genomes_names_ids.txt`

Donde: 
- `freq_hmmmodel.tab` es la tabla de frecuencias que sacaste con la línea de comando que mencioné antes. Puedes sustituir la parte de "hmmmodel" por el modelo específico del modelo que estes checando. 
- `genomes_names_ids.txt` contiene el identificador del gen, taxID y nombre del organismo. Esta es una base de datos no tan pesada, asi que la dejare en el repositorio. 

Con esto obtienes `new_freqs.csv` con la que puedes hacer gráficas más fácil de frecuencias de genes encontrados, aunque ten en cuenta que serán más resultados de los que originalmente obtuviste en `freq_hmmmodel.tab` ¿Por qué?

Pasa que la base de datos que usas no viene filtrada para evitar duplicados. Aún así, _sabemos_ (gracias Carlos <3) que los duplicados no son muchos, son solo 5 los cuales ya tenemos identificados en una lista: `duplicados.csv`
