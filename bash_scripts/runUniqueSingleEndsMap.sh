#! /bin/bash

#PBS -o /mnt/scratch/ablackpz
#PBS -l nodes=1:ppn=1,walltime=24:00:00

cd /mnt/scratch/ablackpz

var='Mus_musculus.NCBIM37.65.cdna.all'


module load bioinformatics-MODULES
module load bowtie

bowtie-build $var'.fa' $var'.Index'
bowtie -m 1 $var'.Index' -f $var'.overlappingReads.fa' $var'_unique.map'
