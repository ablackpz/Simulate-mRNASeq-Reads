#! /bin/bash

var='240rep1E1R100G100'

bowtie-build 'DataSet'$var'.fa' 'DataSet'$var'Index'
bowtie 'DataSet'$var'Index' --ff -I 0 -X 1000 -f -1 'DataSet'$var'RandomReadsPair1.fa' -2 'DataSet'$var'RandomReadsPair2.fa' 'DataSet'$var'.map'
#python countGeneNamesPairedEnd.py 'DataSet'$var'.map' 200 'DataSet'$var'.geneLength' 'DataSet'$var'.map.geneExp'
#awk '{print $2}' 'DataSet'$var'.map.geneExp' > 'DataSet'$var'.map.geneExpNum'
#python makeHistogram.py 'DataSet'$var'.map.geneExpNum' 0 20 2 'DataSet'$var'.map.geneExpNum.hist'
#awk '{if ($1 != $7) print $1, $7}' 'DataSet'$var'.map' > 'DataSet'$var'.map.incorrect'
#awk '{if ($1 == $7) print $1, $7}' 'DataSet'$var'.map' > 'DataSet'$var'.map.correct'
#wc -l 'DataSet'$var'.map.incorrect'
#wc -l 'DataSet'$var'.map.correct'