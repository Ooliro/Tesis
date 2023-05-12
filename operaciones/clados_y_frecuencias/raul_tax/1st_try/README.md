# Extrayendo raices y hojas de un arbol de Metazoa

## ¿De dónde salen estas cosas?


Las cosas importantes son dos:


- extract_tax_paths.py
- phyliptree.phy


El script usa un arbol en formato phylip y la paqueteria de biopython. Por ahora debes tener un archivo con el nombre de `phyliptree.phy` en la misma carpeta, asi que descarga tu arbol desde el (NCBI)[https://www.ncbi.nlm.nih.gov/Taxonomy/CommonTree/wwwcmt.cgi] y dale el formato que quieras, pero por ahora es importante el archivo en formato phylip.


# ¿Qué salió mal en este primer intento?

Cuando lo queremos usar para trabajar en `all4one` nos damos cuenta que le faltan al menos 100 especies que tenemos en nuestras tablas finales de HMMER y que necesitamos para poder hacer graficas por clados, por lo que necesitamos de una lista más completa