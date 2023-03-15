#!/usr/bin/env python3

import sys
import pandas
archivo=open(sys.argv[1])

myclades = []

for line in archivo:
    line = line.split("\t")
    if len(line) == 2:
        myclades.append((line[0], line[1]))
    else:
        myclades.append((line[1], line[-1]))

save_file = open('tax_clades.tab', 'w+')

for elemento in myclades:
    linea = elemento[0] + "\t" + elemento[1]
    save_file.write(linea)
save_file.close()
