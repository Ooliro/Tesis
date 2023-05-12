# Catálogo de relaciones filogenéticas de quitina sintasa en animales

## Introducción

Puedes consultar la diapositiva de esta introducción [aqui](Tesis (Big Picture).pdf)

Si vemos lado a lado a la Quitina (Ch) y Ácido Hialurónico (AH), notaras que comparten similitudes estructurales. No son idénticas, pero si las comparas al resto de miembros de los glucosaminoglicanos (GAG's) notarás que no solo la estructura es muy similar, también comparten la ubicación de sus proteínas sintasas como proteínas transmembranales.

Esta semejanza es interesante, ya que dentro del gran árbol fiolgenético de metazoos Ch y AH tienen una distribución bien separada acercándose a los vertebrados, ya que Ch suele presentarse en hongos, insectos y crustáceos. A pesar de no estar muy "alejadas" las funciones que despempeñan son distintas, incluso las propiedades físicas de los productos cambian.

Un hecho interesante sobre las proteínas sintasas de estas dos moléculas es que a pesar de que la expresión de AH en un insecto como _D. melanogaster_ es letal, es también posible. 

**¿Qué condiciones se requieren?**

En un artículo publicado en [2004](https://www.jbc.org/article/S0021-9258(19)75452-0/fulltext) se teorizó que la expresión de AH es posible mediante la adición del gen AH al genoma de _D. melanogaster_, sin necesidad de primers o cualquier otro elemento proteico o no-proteico, con la justificación de que la maquinaria necesaria para la síntesis de Ch o AH es la misma esencialmente. Y dados los resultados, ese parece ser el caso!

**¿Dónde o cómo se dió el cambio?**

En este trabajo buscamos en qué punto del árbol filogenético pudo haberse dado el evento de diferenciación. Para ello tomamos datos proteicos del NCBI para todo el reino _Metazoa_, lo pasamos por la herramienta de HMMER (paquete de software gratuito y de uso común para el análisis de secuencias proteicas homólogas) y mediante un "pipeline" diseñado específicamente para este trabajo analizaremos los datos obtenidos para dar respuesta a las preguntas anteriores.

Y si bien encontraremos lo que podría describirse como un "dominio" de quitina sintasa o de sintasa de ácido hialurónico ¿qué son las secuencias que se añadieron/eliminaron en el proceso de diferenciación? Este trabajo incluye, pero no se limita a estas preguntas!


## Información sobre este repositorio

Carpetas, archivos, procedimientos importantes que es importante poder checar en cualquier momento que lo necesite sin la necesidad de tener los archivos conmigo.


## Contenidos
1. Raw_results: Resultados directos de utilizar HMMER, con la herramienta hmmbuild y hmmsearch para obtener los HMM y tablas de resultados estándar y por dominio.

2. gtffs: Listas de números de acceso, geneID y otras cosas para filtrar isoformas.

3. control_lists: Listas que serviran de apoyo y corroboración de datos.

4. new_order: Carpeta de trabajo principal (por ahora)

5. scripts: Scripts probado e implementados en el trabajo de new_order

6. scripts_temp: Scripts sin terminar/refinar/implementar.
