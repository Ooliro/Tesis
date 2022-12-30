# New World Order!

Rehaciendo todo porque drop.duplicates al nivel que lo use nos quitaba información potencialmente importante, rehice todo para tener dos tablas ordenadas de acuerdo con la tabla original de HMMER tanto con datos de la tabla inicial como con los datos del gtf... sobra decir que hay incongruencias importantes pero a final de cuentas me gusta más esta metodología.

### Primera parte: ROM

Dos tablas:

1. ROM_saple.tab
2. ROM_maze.tab

Son tablas originales directamente obtenidas de HMMER

### Segunda parte: Stem, Hefi y Sefi

1. temp_HEFI_saple.csv
2. temp_HEFI_maze.csv
3. HEFI_saple.csv
4. HEFI_maze.csv

Listas temporales para quitar encabezados y colar, sustituir multiples espacios por tabuladores, para acomodar la ultima columna y sea solo una (descripcion del organismo).

5. SEFI_maze.csv
6. SEFI_saple.csv

Listas con los campos específicos (1,3,4,7,18,19,22,23) para una lista de la que podemos extraer información importante. **De aqui sacamos todo lo demás, así que si necesitas un punto de inicio para empezar a parsear de manera distinta los datos listos para trabajar, las tablas que necesitas son las que empiezan con SEFI**

### Tercera parte: Placenta (se que es un nombre raro)

Ocupamos dos tipos de lista:

- Lista GTF
- Lista Sefi

La única manera de relacionar estas dos listas es con el número de acceso (Col. 1 en Hefi) y con el Protein ID (Col. 4 en GTFs). El punto inicial es ordenar tus datos GTF de acuerdo al dado por las listas Hefi:

1. PLAC_gtf_maze.csv
2. PLAC_gtf_saple.csv

Y por otro lado, para tener información complementaria al mismo nivel de estas listas hice los mismo pero al reves! Con las nuevas listas PLAC busqué y ordené las listas Hefi porque... ¿por qué no? Pero aqui pasa algo gracioso, **perdemos secuencias en esta búsqueda en reversa y no estoy seguro de porqué!**

1. PLAC_hefi_maze.csv
2. PLAC_hefi_saple.csv

Nota: No se qué tanto influyó, pero **no debes usar hefi, debes usar SEFI**. Yo usé HEFI y de inicio tiene campos que no me interesan!

Como no se qué pasó, usaremos las listas gtf (PLAC_gtf) para empezar a hacer el filtrado. ¿Por qué? 

1. Porque sobre esta tenemos más información
2. Porque con esta tenemos genID que podemos usar para saber cuántas veces se repiten los genes
3. Porque a partir de estos podemos quedarnos con solo un representante y ver más fácilmente si funciona el filtrado o no.

### Cuarta parte: Cordon

Usando Feene2.py y la columna 1 (GenID) para filtrar las listas PLAC_gtf pude obtener resultados satisfactorios con un solo representante por genID, al menos para Drosophila_melanogaster:

1. COR_maze.csv
2. COR_saple.csv

Con esto podemos empezar a hacer gráficas y responder algunas preguntas:

1. ¿Cuántos genes únicos hay?
2. ¿Cuántos genes hay por genoma?
3. Grafica las frecuencias de estos

### Quinta parte: Gráficas

Necesitamos gráficas para ver la distribución de nuestros datos. En este caso podemos sacar gráficas de frecuencias con las que tal o cual genID se repite. Pero graficar estas frecuencias no es muy revelador en sí. Aún así puedes dar demostraciones gráficas que cómo es que distribuyen tus genes y genomas:

1. temp_GRAF_maze.csv
2. temp_GRAF_maze.csv
3. GRAF_maze.csv
4. GRAF_saple.csv

## Segunda Etapa

Con estas tablas filtradas [Cordon] podemos sacar algunos datos de inteŕes. En primer lugar podemos corroborar con especies control que efectivamente tengamos los genes que se supone deben haber. Para propósito de control usaremos a:

- Drosophila melanogaster
- Homo sapiens
- Danio rerio
- Canis lupus
- Branchiostoma floridae

En cada oportunidad que tengas, ve cómo están distribuidas estas especies, cuántos genes están representados y demás características!

   Para la segunda etapa incluiremos dos columnas más que nos ayudarán a sacar el máximo de información de nuestras listas:

- Longitud de secuencias de aminoacidos
- Taxonomía

A partir de aqui talvez quieras considerar trabajar en Pyhton o R ya que si sigues trabajando con bash terminarás con muchos archivos intermedios y tendrás problema organizandote.

### Longitud de secuencias

Usaremos las columnas de las tablas originales de hmmer para sacar i) las longitudes totales de ese dominio y ii) los intervalos de inicio y fin de acuerdo al alineamiento para agregarlos a las tablas.

   Técnicamente ya tenemos estas tablas, pero están en versión SEFI lo que significa que tenemos los datos de las tablas originales y no los del gtf. Así que tenemos que hacer un par de cosas para poder hacer coincidir estas tablas con las de PLAC. Mi primera solución es la que tenía planeada desde un inicio con PLAC_hefi_ddd.csv que eran los mismo elementos de la tabla de gtf pero con datos de hmmer. Esto para poder hacer un simple copiado y pegado de las columnas que nos interesan. Pero como ya viste perdí secuencias haciendo esta parte de hefi, no se si es error mío por usas las listas Hefi en lugar de SEFI, pero ya veremos.
    
La segunda solución es:

Con:
    COR_ddd.csv
    SEFI_ddd.csv
    
Buscar:
    Número de acceso
    
Cortar:
    Columnas 18 y 19 de SEFI
    
Agregar:
    Columnas cortadas a COR_ddd.csv en orden
