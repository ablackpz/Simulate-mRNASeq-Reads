#! /bin/bash

file1='DataSet144'
file2='DataSet144.130'
fileOut='DataSet144.144130'

python combine-khmer-khmer-results.py $file1'.outMed.idsNums' $file2'.outMed.idsNums' $fileOut'.outMed.idsNums.combine'
python calc-log2-diff-exp.py $fileOut'.outMed.idsNums.combine' $fileOut'.outMed.idsNums.combine.log2ratio'
awk '{print $4}' $fileOut'.outMed.idsNums.combine.log2ratio' > $fileOut'.outMed.idsNums.combine.log2ratio.nums'
python makeHistogram.py $fileOut'.outMed.idsNums.combine.log2ratio.nums' -10 10 2 $fileOut'.outMed.idsNums.combine.log2ratio.hist'