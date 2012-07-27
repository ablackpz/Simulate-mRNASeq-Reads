#! /bin/bash                                                                    

groups='Gallus_gallus.transIdgeneId.txt'
mapped='DataSet232rep2E1R10G100_default.map'
name='Gallus_gallus.allGeneNames.txt'
ref='DataSet232rep2E1R100G100RandomReadsNames.txt'

#awk '{print $1}' $mapped > $mapped'.col1'                                      
#awk '{print $6}' $mapped > $mapped'.col6'                                      
python getGeneReadCountsFromTranscriptMapping2.py $groups $mapped'.col6' $ref $mapped'.col6.geneExp' $mapped'.col1.geneExp'
#cp 'DataSet235rep2E1R100G100_default.map.col1.geneExp' $mapped'.col1.geneExp'
python combine-bowtie-bowtie-refFile-results2.py $name $mapped'.col6.geneExp' $mapped'.col1.geneExp' $mapped'.col6.col1.geneExp.combine'
python calc-log2-diff-exp2.py $mapped'.col6.col1.geneExp.combine' $mapped'.col6.col1.geneExp.combine.log2diff2'
awk '{print $4}' $mapped'.col6.col1.geneExp.combine.log2diff2' > $mapped'.col6.col1.geneExp.combine.log2diff2.nums'
awk '{if ($1 <= 1 && $1 >= -1) print $0}' $mapped'.col6.col1.geneExp.combine.log2diff2.nums' > $mapped'.col6.col1.geneExp.combine.log2diff2.numsWithinPm1'
wc -l $mapped'.col6.col1.geneExp.combine.log2diff2.numsWithinPm1'
#python makeHistogram.py $mapped'.col6.col1.geneExp.combine.log2diff.nums' -19 20 2 $mapped'.col6.col1.geneExp.combine.log2diff.hist'
