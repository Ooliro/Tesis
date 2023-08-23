# Coloreando clados

## Descripción general

El objetivo de esta carpeta es poder tener un archivo de anotación listo y completo para cada árbol que necesitemos visualizar y presentar. Estos archivos de anotación deben tener las características de:

- Modificables
- Fáciles de entender 
- Reproducibles sin mayor intervención del usuario

Y me refiero a *archivo de anotación* a el archivo que una vez cargado a Evolview (o en todo caso ITOL) nos permita visualizar la distribución de todos los clados que queramos mediante colores y etiquetas legibles en el árbol filogenético en proceso. Debido a los contratiempos que tenemos con el procesamiento del "árbol" de NCBI Taxonomy (el cual usamos como base para la clasificación de clados en _Lolipop_) forzozamente necesita de la revisión humana para corroborar que efectivamente todas las especies halladas hayan sido clasificadas con un clado. El script `clean_pos_tree.py` (versión limpia y sin comentarios de `pos_tree.py`) sólo nos ayuda a tener una lista con relación más directa entre TAG:Clado, por lo que aún falta elaborar el archivo de anotación final que simplemente cargaremos a Evolview para tener árboles listos para presentar. Sin embargo, es probable que necesitemos más de un archivo de anotación para poder ver clados de importancia para nuestra investigación, por lo que por ahora están contemplados los siguientes archivos de anotación:

- Completo - Todos los clados coloreados y representados en el árbol
- Amphioxus:Mammalia
- Insecta:Intermedio:Mammalia

## Primer paso: correr `clean_pos_tree.py` para ver qué clados *no están representados*

Como dije antes, en _lolipop_ por alguna razón no están completas las clasificaciones de clados, por lo que hay que añadir las que falten para que nuestro archivo de anotación esté bien completo. Para esto lo únco que hacemos es correr una vez el script en cuestión y en la misma terminal nos dará qué especies no cuentan con una clasificación de clado... y esta es la parte tediosa. Hay que anotarlas y buscar independientemente cada una en NCBI Taxonomy para asignarle un clado correspondiente a los que ya tenemos. Por ahora parece que ningún clado nuevo es agregado, así que puedes tomar de referencia la lista de _lolipop_ (terminación en cc.csv) y sus clados para orientarte sobre qué nivel darle a tus nuevas anotaciones.

Cabe recalcar que estas nuevas anotaciones debes hacerlas de preferencia en la lista anteriormente mencionada, hasta el final y teniendo cuidado de que sea el modelo y base correspondiente (cgch ó scf; m ó s), para poder tener un control de cuáles especies fueron agregadas después de este primer intento.

## Segundo paso: correr `clean_pos_tree.py` por segunda vez y corroborar que ninguna especie falte

Y si lo hiciste bien, ya no debería aparecer ninguna especie en la terminal...

yay!

## Tercer paso: Asignar un color a cada clado

Esto es suficientemente obvio, a cada clado que tengas le asignarás un color en formato HEX.


