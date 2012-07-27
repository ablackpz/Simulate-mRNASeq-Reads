#! /bin/bash                                                                    

groups='Mus_musculus.transIdgeneId.txt'
mapped='test.map'

#awk '{print $1}' $mapped > $mapped'.col1'                                      
#awk '{print $8}' $mapped > $mapped'.col8'                                      
python getGeneReadCountsFromTranscriptMapping2.py $groups $mapped'.col8' $mapped'.col1' $mapped'.col8.geneExp' $mapped'.col1.geneExp'
python combine-bowtie-bowtie-results.py $mapped'.col8.geneExp' $mapped'.col1.geneExp' $mapped'.col8.col1.geneExp.combine'
python calc-log2-diff-exp.py $mapped'.col8.col1.geneExp.combine' $mapped'.col8.col1.geneExp.combine.log2diff'
awk '{print $4}' $mapped'.col8.col1.geneExp.combine.log2diff' > $mapped'.col8.col1.geneExp.combine.log2diff.nums'
python makeHistogram.py $mapped'.col8.col1.geneExp.combine.log2diff.nums' -19 20 2 $mapped'.col8.col1.geneExp.combine.log2diff.hist'
