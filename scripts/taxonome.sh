#!/usr/bin/env sh

echo $1;
echo "
Tabla de taxonomias: $1
";
echo "
USO ESPERADO

Obten la lista de especies y su clado perteneciente mediante un "árbol" de taxonomia.

Se esperan 4 Clados: Arthtopoda, Mollusca, Chordata y Nematoda


";

cat $1 | rev | cut -f1 | rev | tail > species.temp
cut -f1 $1 > clade.temp

paste species.temp clade.temp > clade_tax.tab

mkdir del_me

mv clade.temp del_me/
mv species.temp del_me/

echo "ya we"
