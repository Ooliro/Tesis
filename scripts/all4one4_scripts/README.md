# Uso de all4one, version 4 (Marzo 2023)

Esta es la versión 4 de esta cosa. 

El script principal no cambia mucho, solo agrega una línea para obtener la lista de especies de la tabla de "frequencies.csv" que nos sirve para buscar el árbol de clados. 

Además, "feene" (ahora `unduplicate_freq_count.py`) saca frecuencias y que ocuparemos después en los scripts secundarios de "intab_clades" para poder sacar tablas de frecuencias por clado más fácil.

## Scripts necesarios:

- all4one4.sh
- unduplicate_freq_count.py
- whtspc4tabV2.py

### Archivos que ocupas:

- Tabla de resultados "cruda" de hmmsearch por dominios (--domtblout)
- Base de datos GTF (Latest Refseq + Complete Genomes + Chromosomes + Scaffold)

## Scripts secundarios (intab_clades)

- cld_craft_1.py
- cld_craft_2.py

### Archivos que ocupas:

- Árbol de clados de tus secuencias (Revisa "intab_clades" para mas información)
- Frecuencias de especies a trabajar ("frequencies.csv" obtenido de all4one)

