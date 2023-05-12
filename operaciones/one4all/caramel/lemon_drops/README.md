# The Purge

Esto se hace solo como curado de secuencias para armar un árbol filogenético más preciso (y fácil de procesar). En un alineamiento al azar de 100 secuencias de un archivo obtenido mediante `caramel` nos topamos con que al menos 6 secuencias eran exactamente idénticas, pero con anotaciones distintas y, por consiguiente, diferentes especies. 

Técnicamente no hay nada de malo en eso, de hecho es interesante lo conservadas que pueden estar secuencias, pero para análisis y reconstrucción de filogenia tenemos que quitar estas secuencias repetidas (y anotando cuáles se quitaron y a cuál es idéntica, esto servirá en la discusión de resultados)

## Parte 1 - Filtrado y anotado de secuencias idénticas

**Objetivo:Si hay secuencias idénticas, conserva solo una de ellas y anota en otro archivo cuáles son las que se quitaron** 

### CD-HIT

CD-HIT stands for Cluster Database at High Identity with Tolerance. 

The program (cd-hit) takes a fasta format sequence database as input and produces a set of 'non-redundant' (nr) representative sequences as output. In addition cd-hit outputs a cluster file, documenting the sequence 'groupies' for each nr sequence representative. The idea is to reduce the overall size of the database without removing any sequence information by only removing 'redundant' (or highly similar) sequences. This is why the resulting database is called non-redundant (nr). Essentially, cd-hit produces a set of closely related protein families from a given fasta sequence database.

CD-HIT uses a 'longest sequence first' list removal algorithm to remove sequences above a certain identity threshold. Additionally the algorithm implements a very fast heuristic to find high identity segments between sequences, and so can avoid many costly full alignments.

With recent developments, cd-hit package offers new programs for DNA sequence clustering and comparing two databases. It also has lots of new options for clustering control. 

Lo instalé mediante [conda](https://anaconda.org/bioconda/cd-hit):

`conda install -c bioconda cd-hit`

El uso pensado:

`cd-hit -i input.fasta -o output.fasta -c 0.9 -n 5`

- -i input.fasta: Archivo FASTA de trabajo
- -o output.fasta: Especifica el nombre del archivo que tendrá sólo las secuencias no redundantes
- -c 0.9: Especifica el umbral de identidad. Por ejemplo, el 90% de identidad
- -n 5: Especifica el largo de "palabras" mínima del alineamiento. Mínimo debe ser 5
