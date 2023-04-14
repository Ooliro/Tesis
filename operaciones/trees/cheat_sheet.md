# From SeqIO Manual

## Cargar una secuencia tipo "string"

Con esto puedes hasta pedir la cadena complementaria de una secuencia de ADN!

>>> from Bio.Seq import Seq
>>> my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")


## Mocha parte de la secuencia

Con esto puedes cortar un rango de secuencia específico:

>>> from Bio.Seq import Seq
>>> my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
>>> my_seq[4:12]
Seq('GATGGGCC')

## Carga un archivo fasta para parsear

>>> from Bio import SeqIO
>>> for seq_record in SeqIO.parse("cool_proteins.fasta", "fasta")
...     print(seq_record.id)
...     print(repr(seq_record.seq))
...     print(len(seq_record))
