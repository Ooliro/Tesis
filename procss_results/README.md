# All4One: Archivos resultado 

Encontraras dos carpetas principales para resultados a nivel de Genomas completos y cromosomas (cgch_ops), y a nivel scaffold (scf_ops)

## Descripción general

`All4One` está diseñado para parsear las tablas resultado de HMMER con hits por dominio (--domtblout). Por lo que si deseas utilizarlo, recuerda agregar este argumento a tu linea de comandos para que tengas una tabla parseable por este script.

Lo que obtienes de este script son:

- *all_fields.csv*
  - Archivos con columnas de [1] numero de acceso de proteína,[3] longitud de la secuencia/perfil,[4] nombre de la secuencia/perfil,[7] e-value general,[18] inicio del dominio hallado deacuerdo al alineamiento MEA (Maximum Expected Accuarcy),[19] fin del dominio hallado deacuerdo al alineamiento MEA y [23] la descripción del hit (nombre de la proteína).

- *ok.txt*
	+ Secuencias halladas dentro de la base de datos GTF
	
- *fail.txt*
	+ Secuencias no halladas dentro de la base de datos GTF
	
- *gtf_ordered.csv*
	+ *all_fields.csv* pero capturando la información de la base de datos GTF
	
- *no_duplicates.csv*
	+ Tabla que contiene tus secuencias originales de HMMER pero sin isoformas. Esto es, tu tabla sin genes repetidos (filtrados por GenID)

- *frequencies.csv*
	+ Tabla que contiene el conteo de genes por especie.

- *spp_freq*
  + Especies unicas y ordenadas alfabeticamente. Esta se usa para obtener el árbol de clados en el NCBI (CommonTree) 
