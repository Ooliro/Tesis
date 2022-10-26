# Parsing
## Terminal y AWK
### ¿Qué hiciste para saber qué claves están y no están en tus dos barridos?
El flujo fue algo alborotado y hecho sobre el camino, pero la idea fue aislar los numeros de acceso de los dos barridos hechos sobre la base de datos de cromosomas completos, para luego compararlos y ver qué archivos comparten y cuáles no. Para esto imagino que hay varias maneras, pero lo que hice en este intento #1 siguió el siguiente flujo: 

1. Correr hmmsearch sobre la base de datos de cromosomas completos con los modelos de msaprobs y pfam. Estableciendo específicamente que los archivos de salida sean en forma de tabla y tabla por dominio, ya que estos no incluyen información innecesaria. En este primer intento utilicé el archivo en forma de tabla (--tblout).
2. Esa tabla fue editada para que quitaramos los encabezados para poder parsearlo (las primeras 3 líneas)

`sed '1,3d' tabla1.tab > tabla1_1.tab`

3. Sin los encabezados, puedo manejar el archivo como columnas más manejables. Ahora solo necesitamos la columna de las claves de acceso de ambos barridos (Pfam y MSAProbs), por lo que corremos lo siguiente:

`grep 'XP' tabla1_1.tab | cut -d' ' -f1 > XPs_list.txt`

4. Como precaución simplemente las ordene.

`sort XPs_list.txt > XPs_sortlist.txt`

5. Aqui está el turrón del asunto. Utilizando awk que saqué de [esta pregunta](https://unix.stackexchange.com/questions/120416/set-difference-from-two-files-in-unix) mandé al archivo "joined.txt" las claves de la lista de msaprobs que no están en la lista de pfam. 

`awk 'NR==FNR {key[$1]; next} !($1 in key)' XPs_sortlist_pfam.txt XPs_sortlist_msap.txt > joined.txt`

De por si hay 72 claves más en msaprobs que en pfam (msaprobs= 1882 ; pfam= 1810). El correr este comando nos deja con 157 claves únicas de msaprobs… cuáles son esas?

6. En teoría, tengo las claves que no están contenidas en el barrido de pfam, por lo que al no solo contener buena parte de los resultados de pfam sino agregar unos cuantos más con msaprobs, tengo un modelo decente. Pero ¿qué pasa con esas claves únicas de msaprobs? las podemos aislar y ver así:

`grep -f joined.txt tabla1.tab > none_list.tab`

Así usamos el archivo con las claves únicas para buscarlas en la lista inicial para saber qué especie son y los e-value de estos.

## ¿Qué podemos hacer para mejorar esta vista?
- Ordenar nuestra lista ahora por el valor de e-value
- Dejar solo los valores de e-value, número de acceso y especie. Ya sabes, para tener una tabla más limpia y con sólo la información que nos interesa.
- Buscar listas de isoformas, para reducir secuencias. 

## ¿Cómo podemos separar el archivo de salida en columnas de interés?
`tr -s ' ' < archivo.txt | cut -d ' ' -f 8`

Funciona a medias. Ya que toma como delimitador los espacios, te separa bien todo menos el nombre (Description of target) porque está separado por espacios. Se soluciona con:

No se, por el momento no necesito tanto detalle. Puedo sacar la información que necesito con el archivo así como está, en caso de necesitar un archivo más simple con resultados más simples ya veŕe cómo hacerlo. Por el momento el doc dice que se pueden hacer varios cortes y después unirlos, a mi de rápido se me ocurre cortar 5-9 columnas más fuera de la columna 19 para poder capturar los nombres cortados.

Sólo especifica la columna a cortar en cut, con el número de field. Por defecto este comando aisla la columna del e-value en el grupo "Best 1 domain". Los encabezados son:
1. target name *
2. accession  
3. query name   *              
4. accession    
5. [Full sequence] E-value  
6. [Full sequence] score  
7. [Full sequence] bias   
8. [Best 1 Domain] E-value * 
9. [Best 1 Domain] score  
10. [Best 1 Domain] bias   
11. [Domain Number Estimation] exp 
12. [Domain Number Estimation] reg 
13. [Domain Number Estimation] clu  
14. [Domain Number Estimation] ov 
15. [Domain Number Estimation] env 
16. [Domain Number Estimation] dom 
17. [Domain Number Estimation] rep 
18. [Domain Number Estimation] inc 
19. Description of target *

## Python sets
Ya tengo una forma de hacerlo, pero ni idea si está bien hecha :v
Para comprobar que lo que hice está bien (y para explorar otras formas de trabajar los datos) utilizaremos python sets. También podemos usar pandas para crear el data frame pero me dio "parsing errors" y no tengo ganas de andar buscando soluciones por ahora, así que después de usar python sets, probaré con pandas.

El flujo de trabajo va algo así:
1. Aislamos de la hoja de resultados los números de acceso de las tablas de msaprobs y pfam. No usaré grep por el error a en las notas de este apartado, por lo que solo quitare las primeras 3 lineas del archivo original de salida, para luego cortar y guardar solo la primera columna en un solo archivo de texto.
       
       ` sed '1,3d' tabla1.tab > tabla1_1.tab
       cut -d' ' f-1 tabla1_1.tab > msap_targetlist.txt`
       
2. Convertimos esta las cadenas de caracteres que son nuestros archivos target a listas. Puedes hacerlo con split(): 

`tab1 = open(r'/home/raulrosas/Documentos/IFC/Trials/Lab/LuvLab/Parsing/Python_Sets/msap_targetlist.txt')

msaprobs = tab1.read()
msaprobs= msaprobs.split('\n')
tab1.close()

tab2 = open(r'/home/raulrosas/Documentos/IFC/Trials/Lab/LuvLab/Parsing/Python_Sets/pfam_targetlist.txt')

pfam = tab2.read()
pfam = pfam.split('\n')
tab2.close()`

3. Convierte estas listas a sets con set():

    `set_msaprobs = set(msaprobs)
      set_pfam = set(pfam) `

4. Con estos sets estamos para empezar a hacer operaciones. Las que haremos serán unión, intersección y diferencias:

`union = set_pfam | set_msaprobs
intersección = set_pfam & set_msaprobs
dif1 = set_msaprobs - set_pfam
dif2 = set_pfam - set_msaprobs `

5. Observa los resultados:

Unión = 2,025
Intersección = 1,771
Dif1 = 162
Dif2 = 92

### Python Sets: Notas
a) Desde ya me di cuenta que la primera corrida con la Terminal y AWK tiene un error: busca XP's cuando también hay resultados que inician con NP's. **Me faltan resultados**

## Conda: Intervene
1. Instala miniconda
2. Instala intervene con mamba, creando un nuevo ambiente

` conda install -c conda-forge mamba
mamba create -n intervene -c bioconda intervene
conda activate intervene`

3. Con intervene activado, corre:

`intervene venn --type list --save-overlaps -i *target*`

4. Los archivos de resultados se guardan en la carpeta "Intervene_results"

## Reorganizando la tabla de resultados de HMMER

Hay un problema que nos evita tomar información de utilidad y ordenarla en otra tabla: las tablas de resultados de hmmsearch están separadas por varios espacios. Cosa que visualmente no hay gran problema pero para pedirle a bash que lo extraiga es... complicado.

La solución que se me ocurrió en un momento de iluminación fue:

### Solución 1

#### Paso 1

Reemplaza todos los espacios en blanco múltiples por solo uno. Seguiremos este [truco con python](https://stackoverflow.com/questions/37445285/how-to-best-replace-multiple-whitespaces-by-one-in-python) para sustituir multiples espacios en blanco por solo uno. Básicamente:

`import re

tab = open(r'/home/raulrosas/Documentos/IFC/Pruebas/tab_test_nol.tab', 'r')

hmm_tab = tab.read()

tab.close()

hmm_tab = re.sub(' +', ' ',hmm_tab)

hmm_tab # Aqui ya solo tiene un espacio que separa texto... progeso?

save_tab = open('clean_tab.tab','w+')

save_tab.writelines(hmm_tab)

save_tab = save_tab.close()
`

#### Paso 2

Ahora reemplazar ese espacio simple por tabs. Quise hacerlo con sed pero no me acuerdo muy bien como se hace, si me acuerdo lo pongo si no lo pongo como me salió con AWK:

`awk -F'[[:blank:]]' -v OFS="\t" '{$1=$1; print}' input.txt > output.txt`

#### Paso 3

Ahora prueba cortar columnas especiales. Puede que para esto necesitemos quitar los "-" guiones intermedios sin quitar los guines importantes en los e-value. Pero no es necesario ya que podemos ya con este archivo cortar nuestras columnas de interés. Así que ¿qué te parece si enumeramos columnas?:

`head -1 file.tab | sed 's/\t/\n/g' | cat -n > wowo.txt`

Con eso solo restaría identificar qué columnas quieres... y qué son cada una claro. Eso lo puedes hacer a mano o que te enseñen una forma menos elaborada de hacer todo esto.

### Script de Python: whtspc4tab.py

En este mismo repositorio puedes encontrar la carpeta rm_whtspc. Contiene el script de python ejecutable desde terminal para sustituir los múltiples espacios en blanco por tabuladores. 
	Aún así dejaré la primera solución aquí por si la necesitamos de referencia.