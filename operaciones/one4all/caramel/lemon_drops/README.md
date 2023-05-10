# The Purge

Esto se hace solo como curado de secuencias para armar un árbol filogenético más preciso (y fácil de procesar). En un alineamiento al azar de 100 secuencias de un archivo obtenido mediante `caramel` nos topamos con que al menos 6 secuencias eran exactamente idénticas, pero con anotaciones distintas y, por consiguiente, diferentes especies. 

Técnicamente no hay nada de malo en eso, de hecho es interesante lo conservadas que pueden estar secuencias, pero para análisis y reconstrucción de filogenia tenemos que quitar estas secuencias repetidas (y anotando cuáles se quitaron y a cuál es idéntica, esto servirá en la discusión de resultados)

## Parte 1 - Filtrado y anotado de secuencias idénticas

**Objetivo:Si hay secuencias idénticas, conserva solo una de ellas y anota en otro archivo cuáles son las que se quitaron** 

### CD-HIT

Lo instalé mediante [conda](https://anaconda.org/bioconda/cd-hit):

`conda install -c bioconda cd-hit`

El uso pensado:

`cd-hit -i input.fasta -o output.fasta -c 0.9 -n 5`

- -i input.fasta: Archivo FASTA de trabajo
- -o output.fasta: Especifica el nombre del archivo que tendrá sólo las secuencias no redundantes
- -c 0.9: Especifica el umbral de identidad. Por ejemplo, el 90% de identidad
- -n 5: Especifica el largo de "palabras" mínima del alineamiento. Mínimo debe ser 5
