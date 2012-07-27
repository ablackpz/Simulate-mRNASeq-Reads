#! /bin/bash

refName='Gallus_gallus.WASHUC2.63.cdna.all'
readName='Gallus_gallus.WASHUC2.63.cdna.all.overlappingReads'

#bowtie-build $refName'.fa' $refName'.Index'
#bowtie -f -a $refName'.Index' $readName'.fa' $refName'.map'
awk '{if ($1 < $6) print $1,$6; else print $6,$1}' $refName'.map' | sort | uniq > $refName'.map.cols16.sortUniq'
python getTranscriptFamilyGroups.py $refName'.map.cols16.sortUniq' $refName'.map.cols16.sortUniq.transcriptGroups'