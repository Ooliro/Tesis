# De cero a cien: Todo lo que hemos hecho y el cómo llegamos al final

Volvi a hacer todo en base a la guía que tengo en el repositorio, porque necesitaba el 
campo de la longitud del dominio y a ultimadas cuentas se me hacia más fácil asi. El 
flujo lo voy a omitir, solo te dejo claro que los últimos con los que vas a trabajar 
para sacar números de acceso son los que tienen "feene" en el nombre. 

## THE PLAN

Necesitamos una lista o un diccionario que tome el GeneID, Acc mRNA, ProtID y el
tamaño de cada splicing alternativo. Recuerda que este diccionario o lista debe ser accesible
para que pueda:

1. Tener todas las formas de mRNA o transcritos disponibles en el RefSeq para un gen en especial
2. Tener los tamaños de cada splicing
3. Ordenar que solo la más grande de las formas de splicing se quede en la lista de resultados

Para eso tenemos **un plan** GTF > hmmer > Nexus > Undergrad > Teacher > [Senior]

EL PLAN es tener dos listas: la primera (GTF) será la que generamos con Carlos que tienen nombre del gen, GeneID, TranscritoID, ProteinID y organismo; la segunda (hmmer) que es la lista reducida que obtive con Feene.

Estas listas serán utilizadas para tener una tercera lista intermedia (Nexus) que en un principio solo tendrá la información de la lista GTF, ya que el filtro será sobre esa CON la lista hmmer, que deberá tener la misma longitud de esta última. Perderá los e-values temporalmente, por lo que tendremos que pegarsela después. Así tendremos la lista Nexus con la información de la lista GTF, guiado por los resultados de la lista hmmer + e-values de hmmer.

LUEGO empieza lo interesante. Con esa lista Nexus sacaremos una cuarta y quinta lista más: una con solo un representante por cada gen (Undergrad) y otra con las longitudes de cada dominio resultado de hmmer (Teacher) que está en la columna de "tlen" que se obtiene corriendo el adicional --domtblout en hmmsearch. Por último deberíamos tener una sexta y última columna que es la combinación de Teacher y Undergrad: Senior. Senior tendrá solo un representante por gen, con la particularidad de que conservará el representante más grande determinado por las longitudes de Teacher.


### Nexus 

**Lista con información del gtf ordenado de la misma manera que la tabla de resultados de hmmer con e-values y largo de dominios.**


Usar un grep sencillo nos da coincidencias en desorden, y no me salio a la primera en pyhton. Así que recurrí a buscar una solución y encontré esta:

    `$ for S in $(cat file2 | awk '{print $1}'); do grep $S file1; done`
    
Donde:

file1: Archivo en el que buscara coinicidencias # gtfs.csv por ejemplo
file2: Archivo que determinara el orden de las coincidencias halladas # hmm_maze.csv por ejemplo. Que solo tiene los los números de acceso en el orden de la lista original.

### Undergrad y Teacher

**"Teacher" será usada para acomodar a Nexus con las longitudes de dominio obtenidas por hmmsearch (Nexus+tlen). Al mismo tiempo necesitamos otra tabla donde tengamos un solo representante por gen. Es decir, Nexus debe pasar por un filtrado para que cada genID que posea sea reducido a 1. **
