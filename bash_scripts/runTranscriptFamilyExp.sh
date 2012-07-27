#! /bin/bash                                                                    

groups='Gallus_gallus.WASHUC2.63.cdna.all.map.col1and6.sortUniq.transcriptGroupsOneToOne'
mapped='DataSet232rep3E1R10G100_default.map'
name='Gallus_gallus.allTfamNames.txt'
ref='DataSet232rep3E1R100G100RandomReadsNames.txt'

#awk '{print $1}' $mapped > $mapped'.col1'                                      
#awk '{print $6}' $mapped > $mapped'.col6'                                      
python getTranscriptFamilyReadCountsFromTranscriptMapping.py $groups $mapped'.col6' $ref $mapped'.col6.tfamExp' $mapped'.col1.tfamExp'
python combine-bowtie-bowtie-refFile-results2.py $name $mapped'.col6.tfamExp' $mapped'.col1.tfamExp' $mapped'.col6.col1.tfamExp.combine'
python calc-log2-diff-exp2.py $mapped'.col6.col1.tfamExp.combine' $mapped'.col6.col1.tfamExp.combine.log2diff2'
awk '{print $4}' $mapped'.col6.col1.tfamExp.combine.log2diff2' > $mapped'.col6.col1.tfamExp.combine.log2diff2.nums'
awk '{if ($1 <= 1 && $1 >= -1) print $0}' $mapped'.col6.col1.tfamExp.combine.log2diff2.nums' > $mapped'.col6.col1.tfamExp.combine.log2diff2.numsWithinPm1'
wc -l $mapped'.col6.col1.tfamExp.combine.log2diff2.numsWithinPm1'
#python makeHistogram.py $mapped'.col6.col1.tfamExp.combine.log2diff.nums' -19 20 2 $mapped'.col6.col1.tfamExp.combine.log2diff.hist'
