#!/bin/sh -login
#PBS -o /home/ablackpz/
#PBS -l nodes=1:ppn=1,walltime=1:00:00

$var1='292rep1'
$var2='100'

module load bioinformatics-MODULES
module load SOAP2
soap -a 'DataSet'$var1'E1R100G100RandomReads.fa' -D 'DataSet'$var1'E1R'$var2'G100.fa.index' -o 'DataSet'$var1'E1R'$var2'G100_soapAln'