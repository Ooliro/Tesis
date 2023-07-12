# Evolview

## Anotación por hojas 

Esta parece ser una herramienta más fácil de manejar para poder colorear los árboles. Los _headers_ que identifican a estos archivos de anotación son mucho más sencillos y son igual de visualmente llamativos. Limita un poco las formas en las que puedes cambiar los colores y el cómo lo coloreas pero vale la pena.

`leaf background color
mouse	red
human   yellow
rat     blue`

Con este tipo de anotación puedo utilizar la tabla que sale de `pos_tree.py` que nos da una tabla que originalmente era para ITOL que nos da el tag de cada especie con su clado al que pertenece. Con esto puedo asignar un color a cada clado que hay (en teoría hay alrededor de 27 clados = 27 colores) y tener una lista de anotación más sencilla de elaborar.

## Anotación por grupos

Esta sería lo que ocuparíamos pero parece que los rangos deben ser especificados de inicio-fin dentro del árbol, no necesariamente diciendole "toma todos los que tienen X y colorealos de Y", tienes varios ejemplos a usar en su [manual](https://www.evolgenius.info/help/dataset/grouplabel/). Por ahora me gusta más el estilo 2,3 y 4 que tienen el formato siguiente:

### Estilo 2

!grouplabel	style=2,color=pink,show=1,marginPCT=0.05,fontsize=14,fontcolor=white,fontitalic=0,textalign=middle,textorientation=horizontal,linewidth=2
!op	0.8
chicken	bkcolor=#404AC3,text=chicken
mouse,rat	bkcolor=green,text=rodent,fontcolor=darkred
chimp,human	bkcolor=#BE4144,text=mammal,textorientation=vertical,linewidth=4,fontsize=16

### Estilo 3

!grouplabel	style=3,color=pink,show=1,marginPCT=0.05,fontsize=14,fontcolor=white,fontitalic=0,textalign=middle,textorientation=horizontal,linewidth=2
!op	0.8
chicken	bkcolor=#404AC3,text=chicken
mouse	bkcolor=green,text=rodent,fontcolor=darkred
rat,human	bkcolor=#BE4144,text=mammal,textorientation=vertical,linewidth=4,fontsize=16

### Estilo 4

!grouplabel	style=4,color=pink,show=1,marginPCT=0.05,fontsize=14,fontcolor=white,fontitalic=0,textalign=middle,textorientation=horizontal,linewidth=2
!op	0.8
chicken	bkcolor=#404AC3,text=chicken
mouse	bkcolor=green,text=rodent,fontcolor=darkred
rat,human	bkcolor=#BE4144,text=mammal,textorientation=vertical,linewidth=4,fontsize=16
