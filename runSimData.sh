#! /bin/bash

fileHandle='DataSet'

for var in {80..89}
do
    printf "%d\n" "$var"
    python ~/software/khmer/scripts/load-into-counting.py $fileHandle$var'.ht' $fileHandle$var'Reads.fa'
    python ~/software/khmer/scripts/count-median-expr.py $fileHandle$var'.ht' $fileHandle$var'.fa' > $fileHandle$var'.out'
    awk '{print $2}' $fileHandle$var'.out' > $fileHandle$var'.outMed'
    bowtie $fileHandle$var'Index' -f $fileHandle$var'Reads.fa'  $fileHandle$var'.map'
#    awk '{print $3}' $fileHandle$var'.map' > $fileHandle$var'.map.genes'
    python countGeneNames.py $fileHandle$var'.map' $fileHandle$var'.map.geneExp'
    awk '{print $2}' $fileHandle$var'.map.geneExp' > $fileHandle$var'.map.geneExpNum'
done