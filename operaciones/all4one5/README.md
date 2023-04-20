# Quinto intento para all4one 

Esta versión será la más completa hasta ahora. Las bases de datos son las descargadas en Marzo de 2023, cualquier cosa estamos usando los archivos dentro de "big-pops" con los criterios que ya te sabes.

## Primer cambio importante: umbral de inclusión en hmmsearch

Damos un umbral de incusión para quitar resultados que tienen valores de **e-value por encima de 0.0001**

`hmmsearch [options] <hmmfile> <seqdb>`

`hmmsearch --domtblout results_raw.tab --cpu 8 -E 0.0001 model.hmm database.txt`

**Donde:**

- _- -domtblout_: Pide los resultados en formato de tabla y con resultados por dominios
- _- -cpu_: Da el número de núcleos a utilizar
- _-E_: Da el valor de e-value máximo a mostrar en las tablas de resultados
- _model.hmm_: El modelo oculto de Markov a utilizar
- _database_: La base de datos a utilizar (refseq a nivel genomas completos y cromosomas; o scaffold) 

