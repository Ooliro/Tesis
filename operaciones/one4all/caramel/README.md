# Árboles filogenéticos

### Comentarios
Para tener un flujo de trabajo más organizado quiero una nueva forma de organizar los datos: conforme avanza el trabajo se crea una carpeta DENTRO del directorio de trabajo, para que conforme avance el parseo la "profunidad" aumente y aumente.

### Objetivo

Obtener un alineamiento múltiple de los dominios identificados por HMMER y armar un árbol filogenético con ellos

## Procedimiento/Instrucciones

Primero necesitamos los resultados de all4one3. Especificamente el archivo de _`no_duplicates.csv`_ que contiene los resultados de hmmer pero filtrados para excluir isoformas y conservar solo los datos de la base de datos GTF. 

### Fase 1: Creando el subset FASTA

Para crear el subset FASTA de las secuencias de _`no_duplicates.csv`_ ocupamos la base de datos entera del RefSeq para cada análisis que hicimos. En mi caso utilicé dos bases de nivel distinto: 
- Genomas Completos y Cromosomas (cgch) 
- Scaffold (scf)

**Recuerda que también ocupamos dos modelos de Markov distintos (maze y saple), así que terminamos con 4 archivos distintos.**

Tomamos la cuarta columna del archivo de _`no_duplicates.csv`_ y la usamos como archivo BED con `seqtk`para crear un subset de secuencias FASTA pero solo con las secuencias "filtradas".

`
$ cut -f4 no_duplicates.csv > acc.bed
$ seqtk subseq database.fasta acc.bed > new_subseq.fasta
`

**Observaciones**

- cgch
	+ cgchm - Ganamos 4 secuencias sobre el archivo BED
	+ cgchs - Ganamos 7 secuencias sobre el archivo BED

- scf
	+ scfm - Sin cambios
	+ scfs - Sin cambios

### Fase 2: Cortando los dominios identificados en el nuevo subset

Usaremos `bedtools` para cortar los dominios que necesitamos de la base de datos FASTA. Este archivo BED es importante que este organizado de la siguiente manera:

`chr1	1000		2000`

Tres columnas. La primera del nombre del gen/proteína, la segunda del punto de inicio y la tercera del punto de termino.

`bedtools getfasta -fi new_subseq.fasta -bed acc.bed -fo sliced.fasta`

Donde:
- `-fi` Base de datos/subset FASTA
- `-bed` Archivo creado con los puntos de inicio y fin
- `-fo` Nombre del archivo de salida

### Fase 3: Armando el alineamiento múltiple y árbol filogenético

Para alinear esto puedes usar lo que quieras, yo por fresa lo hago desde terminal con msaprobs. Lo puedes instalar mediante conda con:

`conda install -c bioconda msaprobs`

Y el alineamiento:

`msaprobs -o new_ali.fasta sliced_db.fasta`


Donde: 
- `new_ali.fasta` es el nombre de tu nuevo alineamiento
- `sliced_db.fasta` que es el archivo FASTA con dominios recortados.

**Nota Importante: Este proceso es demandante en cuanto a poder de computo, o lo haces en un servidor web como _Bioinformatics Toolkit_ o en una estación de trabajo con buenas especificaciones**

Y finalmente para armar el árbol filogenético:


## Diagrama de flujo

Así mismo, ¿qué tal un diagrama de flujo en forma de árbol?

+ Storytelling
	* all_fields(hmmer)
	* no_duplicates
		- Subsecuencias
			+ Rangos
			+ Fasta subset
			
			
## Road to Wrestlemania!

Tengo un desorden aqui y olvidé hacer algunas modificaciones a los archivos iniciales, así que dejaré aqui el rumbo **tentativo** a tomar. Los cambios más grandes se harán probablemente sobre `pre_tree.sh`.

1. `all_fields.csv` Estos archivos específicos a base de datos y HMM usado necesitan un primer filtro de e-values donde sólo nos quedemos con aquellos menores a 0.0001, osea:

`awk '$7 < 0.001' input.txt > output.txt`

2. `pre_tree.sh` Nos da archivos  necesarios para obtener una sub-base de datos derivada del refseq donde conservamos solo los dominios identificados para las secuencias de hmmersearch: `domdb.fasta`. Este lo filtraremos con _BED.diff_ que es un archivo específico para cada db y HMM que nos da el tamaño de cada dominio para conservar aquellas secuencias que tengan un dominio mayor a 200 a.a.

	2.1. Cambiamos las etiquetas de los FASTA para que quepan dentro del formato Phyilip y sean más fáciles de identificar
	
3. Por último, usamos CD-HIT para quitar secuencias "idénticas"

El archivo resultante de todos estos filtros podremos alinearlo con **msaprobs**, para luego visualizarlo y editarlo, de ser necesario, antes de pasarlo a **RaxML** para armar el árbol filogenético.
