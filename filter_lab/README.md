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

`$cat saple_tabbed.csv | cut -f1,4,7,12,13,23- > saple_fields.csv`

	A.a) maze_fields - "maze_tabbed.csv" pero solo con los campos 1,4,7,12,13 y 23
	B.b) saple_fields - "saple_tabbed.csv" pero solo con los campos 1,4,7,12,13 y 23 

### Archivo con columnas separadas adecuadamente

	C) maze_hefi.txt (msaprobs)
	D) saple_hefi.txt (pfam)
	

	
	
