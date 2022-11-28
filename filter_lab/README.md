# Registro de actividad
## Queremos quitar especies con isoformas repetidas!

### Archivos iniciales

	1. Maze - Tabla de dominios obtenida con hmmsearch utilizando el HMM creado con el alineamiento de msaprobs.
	2. Saple - Tabla de dominios obtenida con hmmsearch utilizando el HMM descargado de Pfam.

### Archivos consiguientes

	A) maze_tabbed.csv - "Maze" pero sin encabezados ni colas, separado por tabuladores.
	B) saple_tabbed.csv - "Saple" pero sin encabezados ni colas, separado por tabuladores.
	

### Archivos con campos específicos

Comando de ejemplo: 

`$cat saple_tabbed.csv | cut -f1,3,4,7,12,13,23- > saple_fields.csv`

	A.a) maze_fields - "maze_tabbed.csv" pero solo con los campos 1,,3,4,7,12,13 y 23
	B.b) saple_fields - "saple_tabbed.csv" pero solo con los campos 1,3,4,7,12,13 y 23 

### Archivo con columnas separadas adecuadamente

	C) maze_hefi.txt (msaprobs)
	D) saple_hefi.txt (pfam)
	
### Archivos finales listos para examinar y generar graficas
	
	E) maze_feene.csv
	F) saple_feene.csv
	
## Comandos y scripts para seguir el flujo de trabajo

- Archivos iniciales:
  	
	`hmmsearch --domtblout domt.tab --tblout simplt.tab hmm_file.hmm database.faa`
	
- Archivos consiguientes:

	`egrep -v "^#" domt.tab > noheadtail.tab`
	
	`ipython whtspc4tab.py
	Files Absolute path: your/own/path/to/file.tab`
	
- Archivos con campos específicos:

	`cat domt.tab | cut -f1,3,4,7,12,13,23- > dominion_fields.csv`
	
- Archivos con columnas separadas adecuadamente:

	`cut -f 6- dominion_fields.csv | sed 's/\t/ /g' | sed 's/,/ /g' > description.txt`
	
	`cut -f -5 dominion_fields.csv > data.txt`
	
	`paste data.txt description.txt > complete_dominion.csv`
	
- Archivos finales listos para examinar el flujo de trabajo:

	`ipython Feene.py
	Files Absolute Path: your/own/path/to/file.csv`
	
	En este punto tendrás un conteo de tus resultados antes y después de pasarlas por el filtro de duplicados tomando como referencia la última columna de nombres y genes... en teoría.
	
	`feene.csv`
	
	A estas alturas puedes cambiar el nombre para tener todo en orden, y mover el resto de archivos intermediarios a una nueva carpeta de seguimiento.
