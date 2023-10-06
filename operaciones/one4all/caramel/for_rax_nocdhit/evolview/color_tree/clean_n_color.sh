#!/usr/bin/env sh

# We will use the uniqueseq.phy file from IQTree to clean up our annotation file, since this is necessary for ITOL to use it properly
# First argument: IQTree uniqueseq.phy file that contains the filteres sequences contained in the tree
# Second argument: pre-tree annotation file (itool_anotation.txt) containing the COD and clade

for S in $(cat $1)
