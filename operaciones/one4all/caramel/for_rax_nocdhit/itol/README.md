# Coloreado de archivos de anotación de ITOL utilizando DATASETS_COLORSTRIP

USO:

`$ ipython chromationV3.py [itol_annotation.txt]`

NOTAS:

- Recuerda que `itol_annotation.txt` es un nombre temporal... que no he cambiado porque asi sale de `pos_tree.py`. Ese es el archivo que utilizamos para generar nuestros archivos de anotación.
- Por ahora (versión 3) no añade la leyenda a tu anotación, tienes que agregarlo y modificarlo a mano, no olvides que tus delimitadores aqui también aplican. El ejemplo de leyenda para tu archivo de anotación está aqui mismo con el nombre de `legen_testo.txt`. Las partes que debes/puedes modificar son las que empiezan con "LEGEND" o las que tienen un valor temporal de "CATZ".


`chromationITOLV3` utiliza el método de DATASETS_COLORSTRIP para generar varios archivos de anotación. Tienes dos variantes de archivos finales, uno extendido y otro simplificado. El primero te genera una archivo de anotación con todos los clados que diste en _lolipop_, eso se traduce por lo general en más de 20 clados que en un árbol puede que no sean muy visualmente convenientes por lo que no lo recomiendo salvo para tener un árbol más colorido donde puedas ver grupos especiales en comparación con los otros clados. **Recuerda revisar que todos los colores sean diferentes, yo utilice un generador random y me dio un par de colores repetidos y muchos otros demasiado parecidos entre si.**

El segundo archivo de anotación que yo encuentro más útil es el simplificado llamado `ITOL_simplified_clades.txt` que tiene no solo los clados principales (máximo 6), también tiene los valores de los mismos que se añaden además del color. Esto significa que cuando tu lo cargas a ITOL lo coloresa y cuando pasas el mouse sobre un nodo en especial, te aparece una notita que dice qué clado es el que señalas. Lo único que me falta aquí es que no tiene aún en la versión 3 de Enero es un cuadrito de leyenda, para que puedas saber qué color representa qué si necesidad de utilizar el mouse, y esto mismo lo puedes pasar a una imágen donde se vea todo lo relevante.

## Por qué usamos DATASETS y no el formato de COLORED_BRANCHES

Porque no funciona el "normalito". Aún cuando mi archivo de anotación aparentemente no tiene errores y ITOL tampoco se queja de nada no colorea ni hace nada, supongo que ha de ser un bug o algo así. En fin! Utilizar DATASETS es igual de efectivo.

Recuerda que a pesar de que también se puede quejar de que no encuentra x nodo en tu árbol, no debería tener problema coloreando, lo que yo creí era mi problema con mis primeros intentos de coloreado. Por lo que aún si el archivo que cargues no pasó antes por `referenceXuniques.py` para conservar sólo las secuencias que se utilizaron en el árbol deberías tener buenos resultados... salvo por un detalle. Cuando pasas tu lista de secuencias que se supone sólo están en el árbol (es decir las que están anotadas en uno de los archivos de IQTREE como `.uniqs.phy`) algunas ramas no se colorean, **faltan secuencias**. No estoy seguro de porqué, pero al menos si haces esto te quita el error de "_x secuencias no se encontraron_". Tal vez sea error mío en algún punto de la anotación o filtrado, pero no hace gran diferencia.
