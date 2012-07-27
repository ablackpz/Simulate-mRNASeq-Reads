#! /bin/bash                                                                    

groups='Gallus_gallus.WASHUC2.63.cdna.all.transcripts'
mapped='DataSet232rep3E1R10G100_default.map'
name='DataSet232rep3E1R100G100.fa'
ref='DataSet232rep3E1R100G100RandomReadsNames.txt'

#sort $mapped'.col1' | uniq | awk '{print $1,$1}' > $groups

#pr -m -t -s $mapped'.col6' $mapped'.col1' | awk '{print $1,$2}' > $mapped'.col6.col1'

#awk '{print $1}' $mapped > $mapped'.col1'                                      
#awk '{print $6}' $mapped > $mapped'.col6'                                      
python getTranscriptReadCountsFromTranscriptMapping.py $groups $mapped'.col6' 'dummy.txt' $mapped'.col6.transExp' $mapped'.col1.transExp'
awk '{print $1}' $name > $name'.txt'
cp 'DataSet232rep3E1R100G100_default.map.col1.transExp' $mapped'.col1.transExp'
python combine-bowtie-bowtie-refFile-results.py $name'.txt' $mapped'.col6.transExp' $mapped'.col1.transExp' $mapped'.col6.col1.transExp.combine'
python calc-log2-diff-exp2.py $mapped'.col6.col1.transExp.combine' $mapped'.col6.col1.transExp.combine.log2diff2'
awk '{print $4}' $mapped'.col6.col1.transExp.combine.log2diff2' > $mapped'.col6.col1.transExp.combine.log2diff2.nums'
#python makeHistogram.py $mapped'.col6.col1.transExp.combine.log2diff.nums' -19 20 2 $mapped'.col6.col1.transExp.combine.log2diff.hist'
awk '{if ($1 <= 1 && $1 >= -1) print $0}' $mapped'.col6.col1.transExp.combine.log2diff2.nums' > $mapped'.col6.col1.transExp.combine.log2diff2.numsWithinPm1'
wc -l $mapped'.col6.col1.transExp.combine.log2diff2.numsWithinPm1'
#more $mapped'.col6.col1.transExp.combine.log2diff.hist'
#awk '{if ($1==$2) print $0}' $mapped'.col6.col1' | wc -l > $mapped'.truePositives'
#wc -l $mapped'.col1' > $mapped'.totalReadsMapped'
#more $mapped'.truePositives'
#more $mapped'.totalReadsMapped'