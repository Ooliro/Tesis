# Árboles sin CD-HIT

Con "Caramel" tal como está tenemos problemas de brazos largos, soportes estadísticos no muy buenos (>60%) en ramas basales y ultimadamente un árbol no muy confiable. Podemos mejorarlo, y para ello omitiremos la parte del uso de CD-HIT para quitar secuencias similares, ya que quizá porque este quita buena parte de las secuencias iniciales es que tengamos ramas con brazos tan largos y bajos porcentajes de bootstrap. **Lo que buscamos es un árbol con el que podamos estar contentos, con el menor número de brazos largos y con los mejores valores de boostrap posibles**

## Solución 1 - Omitir CD-HIT

Inicialmente se propuso el uso de CD-HIT porque RaxML daba el aviso de que había muchas secuencias "parecidas" o duplicadas. Esto debido a la gran similitud de secuencias con anotaciones distintas, lo que era de esperarse pero con el objetivo de reducir la redundancia decidimos quitar todas aquellas que tuvieran un porcentaje de similitud mayor a 90%, y alinear las secuencias resultantes. Esto redujo en gran medida la cantidad de secuencias que pasarían a Rax, pero dió como resultado árboles con los problemas ya mencionados, por lo que ahora omitiremos completamente el uso de CD-HIT y procederemos con las secuencias tal cual están con los primeros filtros (tamaño de dominio y e-vale). Al ser muchas más secuencias usaremos una herramienta más aparte de RaxML: iqtree. Esta es considerablemente más rápida que RaxML (al menos en las pruebas preliminares) y tiene herramientas que nos pueden dar resultados en menos de una hora (fastbootstrap y alrt) y son igual de útiles.

Las secuencias a utilizar son las resultado de `pre_tree.sh` que nos da aquellas que cumplen con los criterios de tamaño de dominio y valores de e-vale.

### Comandos para iqtree

Para _fastboostrap_  y _alrt_ usamos:

`time iqtree -m MFP -B 1000 -alrt 1000 -s file.fa -T AUTO --redo-tree`

Donde:

- `-m` Da el modelo a utilizar, en este caso es una selección de modelo extendido seguido por inferencia del árbol (osea busca el mejor para nosotros)
- `-B` Es el _fastboostrap_ de 1000 repeticiones. Al ser más rápido y necesitar un soporte estadístico mayor (<95% de preferencia para ser tomado enserio) podemos pedir un número mayor de repeticiones.
- `-alrt`Parte recomendada para el _fastboostrap_ de prueba de ramas individuales
- `-s` Especifica el archivo a usar
- `-T` Detecta automáticamente cuál es la mejor configuración posible para paralelizar el proceso. (Osea cuántos núcleos en paralelo va a usar)
- `--redo-tree` Si ya corriste este árbol una vez, esto solo hará que lo vuelva a correr sin la necesidad de empezar desde cero

Para el bootstrap real:

`iqtree -m MFP -b 100 -s file.fa -T AUTO --redo-tree`

Donde:

- `-b` Opción para calcular las replicas de boostrap, el árbol ML y árbol consenso

## Visualizando y maquillando (en el buen sentido) el árbol

### ITOL (Interactive Tree Of Life)
Con [ITOL](https://itol.embl.de/) que podemos colorear nuestras ramas por grupos, y lo único que necesitamos es un archivo de anotación tipo BED. Esto es:

- Código/Nombre de la rama
- Subgrupo al que pertenece

Este **archivo de anotación** nos sirve para poder analizar la distribución de especies en el árbol más fácil y rápido. Pero este hay que crearlo utilizando otros archivos que ya tenemos: tag.BED (caramel), subdb.fa (caramel) y model_cc.csv (lolipop).

Una de las ventajas de ITOL es que las ramas, colores, gradientes y estilos se pueden cambiar. La desventaja de esto es que los archivos de anotación que no son gratis (la versión paga de ITOL hace mucho más fácil colorear el árbol) son un poco complicados de hacer. Tienen plantillas para cada cosa que quieras hacer, lo que se convierte en muchas plantillas y muchas variables que te dejan colorear a tu gusto, todo disponible en su [página](https://itol.embl.de/help.cgi#intro) con instrucciones y todo.

### Evolview

[Evolview](https://www.evolgenius.info/evolview/#/) es otro de los visualizadores de árboles que pueden manejar nuestros árboles. Tiene funciones similares a ITOL, pero con archivos de anotación mucho más sencillos. Tiene un nivel de personalización menor a ITOL pero es lo suficientemente útil para lo que queremos, con instrucciones más sencillas y una interfaz decente para trabajar.

### Modificaciones post armado de árboles

El script `pos_tree.sh` lo que hace es armar un archivo de anotación que tiene dos columnas: código y clado. Esto con el fin de tener una lista de correlación directa para el árbol con su clado. Lo mismo para poder colorearlos, con esta tabla podemos asignar un color por clado y generar nuestro nuevo archivo de anotación para colores.
