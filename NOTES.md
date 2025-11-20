# Notes:

## Taxa:

## Data:

## Phlorest:

## Cognate coding

Cognate sets are coded as binary characters. To convert the data to multistate characters,
where each character corresponds to a concept and states corresponds to the different
cognate sets grouping lexical items for the concept, you may run `commonnexus`' `characters`
cummand as follows

```shell
$ commonnexus characters --multistatise "lambda c: '_'.join(c.split('_')[:-1])" cldf/data.nex
```
