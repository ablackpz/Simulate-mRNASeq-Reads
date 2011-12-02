#! /bin/bash
fileHandle='DataSet'

for var in {130..130}
do
    printf "%d\n" "$var"
#    awk '{print $8}' $fileHandle$var'Reads.txt' > $fileHandle$var'Reads.txtActual'
    python remove-method-readtxt.py $fileHandle$var'cdhitest90n10Reads.txt' $fileHandle$var'cdhitest90n10.txtActual'
done