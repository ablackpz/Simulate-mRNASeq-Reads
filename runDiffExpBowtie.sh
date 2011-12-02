#! /bin/bash

file1='DataSet144'
file2='DataSet144130'
fileOut='DataSet144.144130'

python combine-bowtie-bowtie-results.py $file1'.map.geneExp' $file2'.map.geneExp' $fileOut'.map.geneExp.combine'
python calc-log2-diff-exp.py $fileOut'.map.geneExp.combine' $fileOut'.map.geneExp.combine.log2ratio'
awk '{print $4}' $fileOut'.map.geneExp.combine.log2ratio' > $fileOut'.map.geneExp.combine.log2ratio.nums'
python makeHistogram.py $fileOut'.map.geneExp.combine.log2ratio.nums' -10 10 2 $fileOut'.map.geneExp.combine.log2ratio.hist'