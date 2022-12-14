# Column Index

## For - -tblout in protein

1. **target name**: The name of the target sequence or profile.

2. **accession**: The accession of the target sequence or profile, or ’-’ if none.

3. **query name**: The name of the query sequence or profile.

4. **accession**: The accession of the query sequence or profile, or ’-’ if
none.

5. **E-value (full sequence)**: The expectation value (statistical significance) of the target. This is a per query E-value; i.e. calculated as the expected number of false positives achieving this comparison’s score for a single query against the Z sequences in the target dataset. If you search with multiple queries and if you want to control the overall false positive rate of that search rather than the false positive rate per query, you will want to multiply this per query E-value by how many queries you’re doing.

6. **score (full sequence)**: The score (in bits) for this target/query comparison. It includes the biased-composition correction (the “null2” model).

7. **Bias (full sequence)**: The biased-composition correction: the bit score difference contributed by the null2 model. High bias scores may be a red flag for a false positive, especially when the bias score is as large or larger than the overall bit score. It is difficult to correct for all possible ways in which a nonrandom but non homologous biological sequences can appear to be similar, such as short-period tandem repeats, so there are cases where the bias correction is not strong enough (creating false positives).

8. **E-value (best 1 domain)**: The E-value if only the single best-scoring domain envelope were found in the sequence, and none of the others. If this E-value isn’t good, but the full sequence E-value is good, this is a potential red flag. Weak hits, none of which are good enough on their own, are summing up to lift the sequence up to a high score. Whether this is Good or Bad is not clear; the sequence may contain several weak homologous domains, or it might contain a repetitive sequence that is hitting by chance (i.e.once one repeat hits, all the repeats hit).

9. **score (best 1 domain)**: The bit score if only the single best-scoring domain envelope were found in the sequence, and none of the others. (Inclusive of the null2 bias correction.]

10. **bias (best 1 domain)**: The null2 bias correction that was applied to the bit score of the single best-scoring domain.

11. **exp**: Expected number of domains, as calculated by posterior decoding on the mean number of begin states used in the alignment ensemble.

12. **reg**: Number of discrete regions defined, as calculated by heuristics applied to posterior decoding of begin/end state positions in the alignment ensemble. The number of regions will generally be close to the expected number of domains. The more different the two numbers are, the less discrete the regions appear to be, in terms of probability mass. This usually means one of two things.On the one hand, weak homologous domains may be difficult for the heuristics to identify clearly. On the other hand, repetitive sequence may appear to have a high expected domain number (from lots of crappy possible alignments in the ensemble, no one of which is very convincing on its own, so no one region is discretely well-defined).

13. **clu**: Number of regions that appeared to be multidomain, and therefore were passed to stochastic traceback clustering for further resolution down to one or more envelopes. This number is often zero.

14. **ov**: For envelopes that were defined by stochastic traceback clustering, how many of them overlap other envelopes.

15. **env**: The total number of envelopes defined, both by single envelope regions and by stochastic traceback clustering into one or more envelopes per region.

16. **dom**: Number of domains defined. In general, this is the same as the number of envelopes: for each envelope, we find an MEA(maximum expected accuracy) alignment, which defines the end points of the alignable domain.

17. **rep**: Number of domains satisfying reporting thresholds. If you’ve also saved a --domtblout file, there will be one line in it for each reported domain.

18. **inc**: Number of domains satisfying inclusion thresholds.

19. **description of target**: The remainder of the line is the target’s
description line, as free text.


-------------------------------------------------------------------


## For - -domtblout

1. **target name**: The name of the target sequence or profile.

2. **target accession**: Accession of the target sequence or profile, or ’-’ if none is available.

3. **tlen**: Length of the target sequence or profile, in residues. This (together with the query length) is useful for interpreting where the domain coordinates (in subsequent columns) lie in the sequence.

4. **query name**: Name of the query sequence or profile.

5. **accession**: Accession of the target sequence or profile, or ’-’ if none is available.

6. **qlen**: Length of the query sequence or profile, in residues.

7. **E-value**: E-value of the overall sequence/profile comparison (including all domains).

8. **score**: Bit score of the overall sequence/profile comparison (including all domains), inclusive of a null2 bias composition correction to the score.

9. **bias**: The biased composition score correction that was applied to the bit score.

10. **#**: This domain’s number (1..ndom).

11. **of**: The total number of domains reported in the sequence, ndom.

12. **c-Evalue**: The “conditional E-value”, a permissive measure of how reliable this particular domain may be. The conditional E-value is calculated on a smaller search space than the independent E-value. The conditional E-value uses the number of targets that pass the reporting thresholds. The null hypothesis test posed by the conditional E-value is as follows. Suppose that we believe thatthere is already sufficient evidence (from other domains) to identify the set of reported sequences as homologs of our query; now, how many additional domains would we expect to find with atleast this particular domain’s bit score, if the rest of those reported sequences were random nonhomologous sequence (i.e. outsidethe other domain(s) that were sufficient to identified them as homologs in the first place)?

13. **i-Evalue**: The “independent E-value”, the E-value that the sequence/profile comparison would have received if this were the only domain envelope found in it, excluding any others. This is a stringent measure of how reliable this particular domain may be. The independent E-value uses the total number of targets in the target database.

14. **score**: The bit score for this domain.

15. **bias**: The biased composition (null2) score correction that was applied to the domain bit score.

16. **from (hmm coord)**: The start of the MEA alignment of this domain with respect to the profile, numbered 1..N for a profile of N consensus positions.

17. **to (hmm coord)**: The end of the MEA alignment of this domain with respect to the profile, numbered 1..N for a profile of N consensus positions.

18. **from (ali coord)**: The start of the MEA alignment of this domain with respect to the sequence, numbered 1..L for a sequence of L residues.

19. **to (ali coord)**: The end of the MEA alignment of this domain with respect to the sequence, numbered 1..L for a sequence of L residues.

20. **from (env coord)**: The start of the domain envelope on the sequence, numbered 1..L for a sequence of L residues. The envelope defines a subsequence for which their is substantial probability mass supporting a homologous domain, whether or not a single discrete alignment can be identified. The envelope may extend beyond the endpoints of the MEA alignment, and in fact often does, for weakly scoring domains.

21. **to (env coord)**: The end of the domain envelope on the sequence, numbered 1..L for a sequence of L residues.

22. **acc**: The mean posterior probability of aligned residues in the MEA alignment; a measure of how reliable the overall alignment is (from 0 to 1, with 1.00 indicating a completely reliable alignment according to the model).

23. **description of target**: The remainder of the line is the target’s
description line, as free text.
