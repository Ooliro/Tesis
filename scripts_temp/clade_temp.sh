#!/usr/bin/env sh

# Agregame a all4one3.sh en cuanto puedas graficar new_clades_f.tab

for S in $(cat tax_clades.tab | awk '{print $3}');
do
    grep $S new_freqs.csv >> cladooos.temp
done

cut -f1 tax_clades.tab > cladx.temp

paste cladooos.temp cladx.temp > new_clades_f.temp

sort -nk 4 -t$'\t' new_clades_f.temp > new_clades_f.tab

mkdir del_me
mv cladooos.temp del_me
mv cladx.temp del_me
mv new_clades_f.temp del_me
