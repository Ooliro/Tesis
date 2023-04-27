#!/usr/bin/env sh

mkdir 4graphs/;

awk '{freq[$1]+=$NF} END {for (clade in freq) print clade, freq[clade]}' $1 > grf.csv;

mv grf.csv 4graphs/;
