#!/usr/bin/env python3

"""This scritp extracts the paths from the leaves to the root
in a ncbi taxonomy tree"""

from Bio import Phylo

# read tree
tree = Phylo.read('phyliptree.phy', 'newick')
tree.ladderize()

# get leaves
leaves = tree.get_terminals()

# get paths
paths = []
for leaf in leaves:
    path = tree.get_path(leaf)
    paths.append(path)

# write to a file

outfile_name = 'taxonomies.txt'

with open(outfile_name, 'w') as outf:
    for path in paths:
        names = [clade.name for clade in path]
        line = '\t'.join(names) + '\n'
        outf.write(line)


print('[DONE] :D')
