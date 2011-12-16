#! /bin/bash
fileHandle='DataSet'
k=10

for var in {130..130}
do
    printf "%d\n" "$var"
    python countKmersTranscriptome.py $fileHandle$var'.fa' $fileHandle$var'.kmerCount' $k
    python countKmersReads.py $fileHandle$var'Reads.fa' $fileHandle$var'.kmerCount' $fileHandle$var'.kmerCount.reads' $k
    python countKmersTranscriptomePerGene.py $fileHandle$var'.fa' $fileHandle$var'.kmerCount' $fileHandle$var'.kmerCount.genes' $k

    grep '>' $fileHandle$var'.fa' | wc -l

done