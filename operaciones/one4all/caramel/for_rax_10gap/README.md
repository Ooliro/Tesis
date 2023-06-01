# Cosas para RAxML

## Scripts ocupados

- pre_tree.sh
- taggin.sh

## Programas ocupados (mediante conda)

- seqtk
- bedtools
- cd-hit
- msaprobs
- RaxML (Compilado localmente)

## Procedimiento general

### Pre-tree v.1

1. ´pre_tree.sh´

Toma tres argumentos: tabla sin duplicados (no_duplicates), tabla de campos de hmmer (all_fields) y una base de datos refseq.
Primero, filtra de la tabla de campos aquellas secuencias que posean un e-value menor a 0.0001 y un dominio (ali) mayor a 200 a.a. 
Segundo, busca su equivalente dentro de la tabla de no_duplicates.
Tercero, prepara las listas BED, sub-base de datos refseq y una archivo FASTA con solo los dominios reconocidos por HMMER (domdb)

2. ´taggin.py´

Toma dos argumentos, una tabla con los nombres completos de las secuencias que necesitamos (subdb) y a la que le queremos cambiar el nombre (domdb)
Toma la primera letra del genero y las dos primeras de la especie, y asigna una un identificador en mayúscula de quitina (C), hialuronano (H) u otro (N)

3. ´CD-HIT´

Conserva secuencias con una similitud de 90% o menor, esto con el propósito de evitar errores en RAX-ML. Las secuencias "quitadas" son anotadas en otra lista

4. ´msaprobs´

El archivo resultante es alineado con msaprobs 

5. ´RAX-ML´

El archivo alineado es ahora pasado a RAX para crear el árbol con un boostrap de 100. Con RAX podemos también crear el árbol consenso!

´raxmlHPC-PTHREADS -T 20 -m PROTGAMMAAUTO -s aligned.phy -n AUTO -p 6112 -b 27 -# 100´

El árbol consenso según el manual se contruye así:

´raxmlHPC -m PROTCATAUTO -J MR -z RAxML_boostrap.T22 -n MR_cons´

Pero el formato resultante no es posible abrirlo. Podemos abrir el boostrap y ver las 100 repeticiones del árbol con [Dendroscope](https://software-ab.cs.uni-tuebingen.de/download/dendroscope/welcome.html) pero por alguna razón no podemos ver el consenso.
Hay que ver aún qué tipo de formato usa para ver cómo podemos visualizarlo, o en todo caso si estamos haciendo algo mal.
