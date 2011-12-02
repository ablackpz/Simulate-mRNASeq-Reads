#! /bin/bash
fileHandle='DataSet'

for var in {131..131}
do
    printf "%d\n" "$var"
    ~/Downloads/bowtie-0.12.0-beta1/./bowtie-build $fileHandle$var'.fa' $fileHandle$var'Index'
done