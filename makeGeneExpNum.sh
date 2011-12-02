#! /bin/bash
fileHandle='DataSet'

for var in {75..78}
do
    printf "%d\n" "$var"
    awk '{print $8}' $fileHandle$var'Reads.txt' > $fileHandle$var'Reads.txtActual'
done