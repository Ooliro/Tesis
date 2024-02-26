# Nueva organización para bases de datos

*Nueva nomenclatura para archivos*

1° Base de datos    [D] = Demi = GC + Ch
                    [I] = Integer = GC + Ch + Scf
                    
2° Modelo Oculto de Markov      [G] = General = Chitin Synthase 2
                                [E] = Específico = Chitin Synthase 2 + Nuestras secuencias
                                
## 1 Paso - HMMER (hmmsearch)

`$ hmmsearch --domtblout ouput_file.tab --cpu 8 markov_model.hmm database.txt`

Tomas a tu base de datos (Demi o Integer) para examinar con el HMM (General o Específico) para tener una tabla de hits por dominio (--domtblout). Dependiendo del equipo que uses puedes usar más o menos de 8 núcleos (--cpu) para el proceso que en promedio toma 1 min 20 seg.


