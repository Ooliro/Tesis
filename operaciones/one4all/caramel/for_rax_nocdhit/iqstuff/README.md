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

## Solución 2 - Aumentar el porcentaje de inclusión en CD-HIT a 95%

Podemos reducir un poco los tiempos de cáculo resultado de la solución 1 sin perder el objetivo de quitar redundancias simplemente aumentando el rango a incluir con CD-HIT. Esto es:

`cd-hit -i input.fasta -o output.fasta -c 0.95 -n 5`

