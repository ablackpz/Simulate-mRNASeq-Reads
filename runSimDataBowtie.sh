#! /bin/bash

var='131'
params='default'

#printf "%d\n" "DataSet'$var'_'$params"
bowtie-build 'DataSet'$var'.fa' 'DataSet'$var'Index'
bowtie --best -f --al 'DataSet'$var'_'$params'_al.map' --un 'DataSet'$var'_'$params'_un.map' --max 'DataSet'$var'_'$params'_max.map' 'DataSet'$var'Index' 'DataSet'$var'Reads.fa' 'DataSet'$var'_'$params'.map'
python countGeneNames.py 'DataSet'$var'_'$params'.map' 100 'DataSet'$var'.geneLength' 'DataSet'$var'_'$params'.map.geneExp'
awk '{print $2}' 'DataSet'$var'_'$params'.map.geneExp' > 'DataSet'$var'_'$params'.map.geneExpNum'
python makeHistogram.py 'DataSet'$var'_'$params'.map.geneExpNum' 0 20 2 'DataSet'$var'_'$params'.map.geneExpNum.hist'
awk '{if ($1 != $6) print $1, $6}' 'DataSet'$var'_'$params'.map' > 'DataSet'$var'_'$params'.map.incorrect'
wc -l 'DataSet'$var'_'$params'.map.incorrect'