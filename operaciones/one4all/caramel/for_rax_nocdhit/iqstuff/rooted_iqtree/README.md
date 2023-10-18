# Árboles de hialuronano con una raíz de quitina

Ya que quedó claro que hialuronano y quitina no son precisamente cercanos, queremos un árbol al que le podamos dar una raíz hipotética y mejorar la visibilidad de nuestros datos.

## Contenidos
rooted_iqtree: Carpeta contenedora de los árboles y alineamientos necesarios para armar los árboles cortados y con su raíz de quitina más cercana.

cgchm/s: Árboles hechos a base de la base de datos de Genomas y Cromosomas Completos, con el modelo específico y original.
scfm/s: Árboles hechos a base de la base de datos de Scaffold, con el modelo específico y orginal.

## Procesamiento
 
El proceso general es editar el alineamiento para que conserve sólo las secuencias que queremos. Recordemos que para poder armar un árbol filogenético necesitamos un alineamiento, y es en este donde podemos hacer cambios antes de pasar a armarlo.

- Alineamiento a usar:
	xxxxx_10gap.fa
Comentarios: Alineamientos múltiples hechos con msaprobs y eliminando gaps con cobertura de 10%

- Herramientas a usar:
	seqtk, sed y grep
Comentarios: Extraemos sólo los encabezados que contienen "H" para usarlos como lista BED en seqtk y extraer sólo esas secuencias del alineamiento original.

- Raíz utilizada: 
	- cgchm_10gap.fa (csepC2)
	- cgchs_10gap.fa (bcoC1) 
		+Son como 11 secuencias nomas de hialuronano XD
	-scfm_10gap.fa (fcaC1)
		+ Son como 5 secuencias XDD
	- scfs_10gap.fa (fcaC1)
Comentarios: La raíz la tomamos con base a la visualización del árbol completo (ITOL). La que esté más cerca a las ramas de hialuronano, tomamos esa.

### Comentarios
Todos lo árboles fueron hechos con el método de _fastboostrap_ EXCEPTO por hyl_M2, que fue hecho con el boostrap real por accidente. Con el número de secuencias que tiene tomó aproximadamente 50 hrs.
