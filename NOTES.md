# Notes


## Data:

> A data set of 285 cognate sets of basic vocabulary was compiled using the sources presented in 2 above. The list of
> basic vocabulary is a modified Swadesh 207-word list that combines the meanings included in Swadesh (1952;1955).
> Meanings that are inappropriate for lowland Amazonian societies such as ‘snow’ and ‘ice’ were excluded from
> consideration. A number of meanings in the original list were substituted for similar culturally appropriate concepts;
> ‘year’ was substituted with ‘dry season’, the local convention used to describe the passing of time, and ‘hound’ was
> substituted with ‘peccary’, a local mammal of high importance for sustenance and spiritual life. Two additional meanings
> were added to the list of basic vocabulary: ‘afternoon’ and ‘brocket deer’. Meanings that were not attested in the
> available data, or that were attested only for members of a single subgroup of languages (most often Waric languages),
> were not included in the final list. The final list of basic vocabulary includes 126 meanings

## Methods:

| Model                                | Score           | Program    | Comment            |
|--------------------------------------|-----------------|------------|                    |
| NeighborNet                          |                 | Splitstree | Hamming            |
| Delta Score                          |                 | Splitstree |                    |
| Q Residual                           |                 | Splitstree |                    |
| CTMC + strict clock                  | −1215.62 ± 0.39 | BEAST1     |                    |
| CTMC + relaxed clock                 | −1209.00 ± 0.12 | BEAST1     | Best fitting Model |
| Stochastic Dollo + strict clock      | −1213.62 ± 0.02 | BEAST1     |                    |
| Stochastic Dollo + relaxed clock     | −1212.82 ± 0.06 | BEAST1     |                    |



## Analysis:

> To quantify the degree of conflicting signal in these data, we calculated two statistics, the δ-score (Holland et al.
> 2002) and the Q-residual (Gray, Bryant, and Greenhill 2010). These two statistics provide a quantitative measure of how
> much conflict (or reticulation) there is in the network. The mean δ-score for these languages was 0.262 (s.d. = 0.033) and
> the mean Q-residual score was 0.016 (s.d. = 0.004).


## Cognate coding

Cognate sets are coded as binary characters. To convert the data to mulistate characters,
where each character corresponds to a concept and states corresponds to the different
cognate sets grouping lexical items for the concept, you may run `commonnexus`' `characters`
cummand as follows

```shell
$ commonnexus characters --multistatise "lambda c: '_'.join(c.split('_')[:-1])" cldf/data.nex
```
