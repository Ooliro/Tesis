#!/usr/bin/env python3


filename = 'sub_cgchm.fasta'

infile = open(filename, 'r')


# son los identificadores ya utilizados
idcounts = {}
species = {}

for line in infile:
    line = line.strip()
    if line == '' or line[0] != '>':
        continue

    # protid

    protid = line.split('.')[0][1:]

    # Chitin or Hyaluronan
    if 'hitin' in line:
        tipo = 'C'
    elif 'yaluronan' in line:
        tipo = 'H'
    else:
        tipo = 'N'

    # species id
    spname = line.split('[')[1].split(']')[0]
    genre, sp, *_ = spname.split(' ')

    spidentifier = genre[0].lower() + sp[:2]

    if spidentifier in species:
        if species[spidentifier] != spname:
                spidentifier = genre[0].lower() + sp[:3]
    else:
         species[spidentifier] = spname

    # numero

    if spidentifier in idcounts:
        number = idcounts[spidentifier] + 1
        idcounts[spidentifier] += 1
    else:
        number = 1
        idcounts[spidentifier] = 1

    final_id = f"{spidentifier}{tipo}{number}"

    print(f"{protid}\t{final_id}")



# Close file
infile.close()
