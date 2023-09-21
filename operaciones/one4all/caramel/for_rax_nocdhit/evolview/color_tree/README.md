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

Ahora cómo dividimos estos colores? Un árbol con hasta 28 colores puede ser algo difícil de leer, incluso con colores vistosos. Así que tenemos alguna sugerencias para probar, aparte del árbol con todos los colores necesarios:

1. Cordados + Todo lo demas
2. Cordados + Protostomos + Todo lo demas
3. Amphioxus + Artrópodos + Vertebrados + NADA (sin colorear lo demás)
4. Quitina + Hialuronano Sintasas

**Nota: Recuerda que estos árboles deben ayudar a explicar la distribución de las sintasas, sin necesidad de un árbol enraizado. Por lo que tal vez tener una gráfica lado a lado de 3. y 4. podría ser una gran diapositiva para ejemplificar los resultados a los que se llegaron.**

### Crea tu lista con colores: chromation.py V1

Como prueba de concepto para tener una lista base lista para adaptar al visualizador de árboles que prefieras tenemos al script `chromation.py` que toma el archivo resultado de `pos_tree.py` llamado, temporalmente, "itool_annotation.txt" que tiene un formato de COD:CLADO.

La principal tarea de `chromation.py` es dar a cada clado un color y anexarlo en forma de una tercera columna. Esto lo hace gracias a un diccionario que debes preparar deacuerdo a cuantos clados tengas por modelo a colorear (si tienes 23 en cgchm o menos en scfs). Los colores se manejan en formato HEX y por ahora sólo son al azar, el punto es que el diccionario mencionado tenga el formato:

"Mammalia": "#FF5733"
"Actinopteri": "#47D147"
    etc...
    
Este diccionario tienes que modificarlo dentro del script en sí. Y al menos en las pequeñas pruebas hechas con esta primera versión, funciona perfectamente. Obtenemos una lista que denominaremos como *"color_ann.txt"* que tiene un formato así:

hsaH3   Mammalia    #FF5733 
apeC2   Actinopteri    #47D147
    etc...
 
 Pero para **evolview** solo ocupamos la primera y tercera columna, asi que solo con cortarlos desde la terminal y pasarlos como archivo de anotación bajo el formato "leaf BK colors" tenemos el resultado que buscabamos: las etiquetas del árbol coloreadas, y visiblemente distintivas para ubicar clados. Excepto que sólo es eso, colores. No hay nomenclatura aún!
 
### Crea tu lista de colores: chromation.py V2
 
_Por términos de "no me confundas, perro" llamaremos a este nuevo script `chromationV2.py` y tendrá los cambios a continuación mencionados.__
 
Como dije antes, el diccionario es lo que hace la magia en general, precisamente porque la tercera columna es "mutable". Es decir, podemos cambiarlo a lo que queramos y esto se va a pasar a la lista final "color_ann.txt" tal y como esté en el diccionario, por lo que podemos modificar el formato de la lista final con pocos pasos y tener un resultado más visiblemente bonito. Para esto nos ayudaremos de los estilos de Evolview para no sólo darles color a las ramas, sino también para poner el clado afuerita de donde estén. La idea es que a diferencia de la V1, esta vez el diccionario tenga un formato así:
 
"Mammalia": "bkcolor=#FF5733, text=Mamíferos, fontsize=16"
"Actinopteri": "bkcolor=#47D147, text= Peces, fontsize=16"
    etc...
 
De nuevo, sólo ocupamos la primera y tercera columna, pero con la diferencia que esta vez el archivo de anotación nuevo necesita de este encabezado especial que puedes modificar en la parte de `style` y elegir entre los estilos de coloreado 3,4 o 5.
 
`!grouplabel style=5, color=pink, show=1, marginPCT=0.05, fontsize=14, fontcolor=white, fontitalic=0, textalign=middle, textorientation=horizontal, linewidth=2`
`!op	0.8`

Estos son los parámetros para poder tener anotación fuera de las ramas. Naturalmente puedes modificar muchas cosas, desde el estilo, color y tamaño de letra hasta el grosor de la misma, cámbialo como te convenga!

#### Corrección de errores

_Este script lo denominaremos como chromation2_1.py_

- Funciona a medias, tenía unos errores de redacción y daba resultados raros. Como nota importante recalco que _!grouplabel_ y los parámetros deben estar separados por un *tabulador*, de otro modo habrá errores al cargarlo en Evolview, y eso incluye al segundo parámetro de opacidad. 

- Por ahora *tienes que editar la ruta absoluta de los archivos a usar* dentro del script, ten eso en cuenta.

- Ahora crea dos archivos de salida: `color_ann` y `second_colorann`. El primero es el archivo que tiene tres columnas de COD,Clado y colores. El segundo archivo tiene sólo COD y color, junto con el encabezado que mencioné antes para poder ser reconocido como coloreado de grupos. **El segundo archivo es el que utilizamos para colorear en evolview.**

- Hay que modificar el color de algunas letras para poder ver claramente qué tiene escrito, en algunos casos se pierde.

- La versión en la que estuve probando estos scripts en **Evolview Ver. 3** porque la edición actual tiene muchos problemas. De primera, no puedo ni entrar a visualizar ni siquierea árboles de demostración. La versión 3 funciona para visualizar, pero para exportar o convertir el árbol en imágen o PDF no funciona. Mi solución para esto sigue en proceso, pero por ahora la opción que veo es hostear evolview en un cliente local... osea instalarlo en mi computadora pero no se aún.

- En la versión 3 tampoco podemos visualizar el árbol en forma circular o sin raíz.

