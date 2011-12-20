#! /bin/bash
fileHandle='DataSet'

for var in {88..88}
do
    printf "%d\n" "$var"
#    awk '{print $8}' $fileHandle$var'Reads.txt' > $fileHandle$var'Reads.txtActual'
    python remove-method-readtxt.py $fileHandle$var'Reads.txt' $fileHandle$var'.txtActual'
done