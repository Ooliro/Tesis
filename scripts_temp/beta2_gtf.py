# -*- coding: utf-8 -*-

"""Version experimental del script para procesar una carpeta completa"""


from sys import argv
import re
from pathlib import Path

def load_sp_dict(filename):
    genomedict = {}
    with open(filename) as inf:
        for line in inf:
            line = line.strip()
            data = line.split('\t')
            genome = data[0].split('.')[0]
            genomedict[genome] = data[1:]
    return genomedict

genomedict = load_sp_dict('genomes_names_ids.txt')

here = Path('.')
input_folder = Path(argv[1])
store_folder = here/'tables'

if not store_folder.exists():
    store_folder.mkdir()


filelist = input_folder.glob("*.gtf")
# expresion regular para procesar archivos
regex = re.compile('.*gene_id "([A-z0-9\-]*)".*transcript_id "([A-z0-9\.]*)".*db_xref "GeneID:([0-9]*)".*protein_id "([A-z0-9\.]*)"')


errores = set([])
for file_ in filelist:
    print(f'[INFO] Working with {file_} .....                             ', end='\r')
    prots = {}
    outfile_name = store_folder/(file_.name+'.tab')
    outfile = open(outfile_name, 'w')
    genomeid = file_.name.split('.')[0]
    with open(file_, 'r') as inf:
        for line in inf.readlines():
            if 'start_codon' not in line:
                continue
            result = regex.findall(line)
            if result:
                # print(*result[0])
                if result[0][-1] not in prots:
                    if genomeid in genomedict:
                        line = '\t'.join(list(result[0]) + genomedict[genomeid]) + '\n'
                        outfile.write(line)
                    else:
                        line = '\t'.join(list(result[0]) + ['NA', 'NA']) + '\n'
                        outfile.write(line)
                        errores.add((genomeid, file_))

                    prots[result[0][-1]] = True
    outfile.close()

with open('errores.txt', 'w') as outf:
    for error in errores:
        outf.write(error[0] + '\t' + error[1] + '\n')

print(errores)

print()
print('[DONE] be happy :D')
