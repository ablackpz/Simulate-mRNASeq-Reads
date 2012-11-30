#! /bin/bash                                               
#PBS -o /mnt/scratch/ablackpz                             
#PBS -l nodes=1:ppn=1,walltime=2:00:00                   

cd /mnt/scratch/ablackpz

var1='292rep3'
var2='20'

module load bioinformatics-MODULES
module load bwa

/opt/software/SAMTools/0.1.18--GCC-4.4.5/bin/samtools view -S -b 'DataSet'$var1'E1R'$var2'G100_aln.sam' > 'DataSet'$var1'E1R'$var2'G100_aln.bam'
/opt/software/SAMTools/0.1.18--GCC-4.4.5/bin/samtools sort 'DataSet'$var1'E1R'$var2'G100_aln.bam' 'DataSet'$var1'E1R'$var2'G100_aln_sort'
/opt/software/SAMTools/0.1.18--GCC-4.4.5/bin/samtools view 'DataSet'$var1'E1R'$var2'G100_aln_sort.bam' > 'DataSet'$var1'E1R'$var2'G100_aln_sort.sam'
awk '{print $1,$20}' 'DataSet'$var1'E1R'$var2'G100_aln_sort.sam' > 'DataSet'$var1'E1R'$var2'G100_aln_sort_nameAssign.2cols'
python getBwaSamParse.py 'DataSet'$var1'E1R'$var2'G100_aln_sort_nameAssign.2cols' 'DataSet'$var1'E1R'$var2'G100_aln_sort_nameAssignParsed.2cols'
awk '{if ($1==$2) print $0}' 'DataSet'$var1'E1R'$var2'G100_aln_sort_nameAssignParsed.2cols' | wc -l > 'DataSet'$var1'E1R'$var2'G100_aln_sort_nameAssign.truePositives'
wc -l 'DataSet'$var1'E1R'$var2'G100_aln_sort_nameAssignParsed.2cols' > 'DataSet'$var1'E1R'$var2'G100_aln_sort_nameAssign.totalReads'