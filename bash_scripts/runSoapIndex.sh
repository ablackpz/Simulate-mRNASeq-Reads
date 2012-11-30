#!/bin/sh -login
#PBS -o /home/ablackpz/Documents/DataSet160
#PBS -l nodes=1:ppn=1,walltime=1:00:00

var1='292rep1'
var2='100'

module load bioinformatics-MODULES
module load SOAP2
2bwt-builder DataSet292rep1E1R100G100.fa