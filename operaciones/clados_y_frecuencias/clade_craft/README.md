# Extrayendo raices y hojas de un arbol de Metazoa

## ¿De dónde salen estas cosas?


Las cosas importantes son dos:


- extract_tax_paths.py
- phyliptree.phy


El script usa un arbol en formato phylip y la paqueteria de [biopython](https://anaconda.org/conda-forge/biopython). Por ahora debes tener un archivo con el nombre de `phyliptree.phy` en la misma carpeta, asi que descarga tu arbol desde el [NCBI](https://www.ncbi.nlm.nih.gov/Taxonomy/CommonTree/wwwcmt.cgi) y dale el formato que quieras, pero por ahora es importante el archivo en formato phylip.

## ¿Dónde obtengo mi árbol en formato phylip?

La lista con la información que necesitas está en la sección de (CommonTree)[https://www.ncbi.nlm.nih.gov/Taxonomy/CommonTree/wwwcmt.cgi], en la parte de Taxonomy del NCBI, pero necesitamos unos pequeños archivos intermedios para llegar desde las especies que buscamos (frecuencias) hasta el árbol del que extraeremos los clados.

_Nota: Los archivos a utilizar vienen de all4one3_

1. Dentro de tu carpeta de resultados, busca el archivo `frequencies.csv` que contiene las especies, taxID y número de ocurrencias dentro de tus tablas a analizar. Con esta solo ocuparemos la primera columna de especies, por lo que la cortaremos y guardaremos como un nuevo archivo llamado... como quieras ponerle. Solo lo ocuparemos para la busqueda dentro del portal de CommonTree asi que ponle como quieras, aqui le pondre la inicial "m" o "s" dependiendo del HMM del que salió la tabla de frecuencias.

`cut -f1 frequencies.csv | sort | uniq > nombre_prron.txt`

2. Con tu archivo resultante nos vamos al CommonTree y en la parte superior verás un botón que dice "Examinar", seleccionalo y carga tu archivo `nombre_prron.txt`, luego presiona "Add from file". Te redireccionará a una lista parecida a un árbol donde ahora seleccionas el nodo de "Animals" y presionas "Choose", donde encontraras un árbol de relaciones filogenéticas de las especies que cargaste, que puedes comprobar con el número de nodos que te resume: deben ser los mismos que el número de especies que cargaste!

3. Para descargarlo solo selecciona el formato en la parte superior de la pantalla (phylip tree) y guardalo.


## ¿Cómo proceso este árbol para que tenga solo las dos columnas de spp y clado?




