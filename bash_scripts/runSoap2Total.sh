#! /bin/bash                                               
#PBS -o /mnt/scratch/ablackpz                             
#PBS -l nodes=1:ppn=1,walltime=2:00:00                   

cd /mnt/scratch/ablackpz

var1='292rep3'
var2='20'

module load bioinformatics-MODULES
module load SOAP2

2bwt-builder 'DataSet'$var1'E1R'$var2'G100.fa'
soap -a 'DataSet'$var1'E1R100G100RandomReads.fa' -D 'DataSet'$var1'E1R'$var2'G100.fa.index' -o 'DataSet'$var1'E1R'$var2'G100_soapAln'