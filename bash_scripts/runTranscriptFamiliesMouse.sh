#! /bin/bash

refName='Mus_musculus.NCBIM37.65.cdna.all'
readName='Mus_musculus.NCBIM37.65.cdna.all.overlappingReads'

bowtie-build $refName'.fa' $refName'.Index'
bowtie -f -a $refName'.Index' $readName'.fa' $refName'.map'
awk '{if ($1 < $8) print $1,$8; else print $6,$1}' $refName'.map' | sort | uniq > $refName'.map.cols18.sortUniq'
python getTranscriptFamilyGroups.py $refName'.map.cols18.sortUniq' $refName'.map.cols18.sortUniq.transcriptGroups'