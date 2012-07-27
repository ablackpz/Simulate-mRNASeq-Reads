# A script to read in a combined file containing an identifer and two columns of numbers that correlate to each other (median and gene expression).  Get the average difference, standard difference, and t.
# Original: 2011.11.23
# Original: A. Black P.
# Last: 2011.11.23
# Last: A. Black P.

# Usage: python calc-individual-differences-t-test.py inputThreeCols.txt output.txt

import sys, makeRandomTestData, math

outfile = open(sys.argv[2], 'w')

print 'Loading/counting data\n'

count = 0
genes = {}
diff = 0
avgDiff = 0
sDiff = 0
tcalc = 0

for newString in open(sys.argv[1]):
    newString = newString.rstrip()
    parts = newString.split('\t')
    genes[parts[0]] = float(parts[1]) - float(parts[2])
    count += 1

for key in genes:
    diff += genes[key]

avgDiff = diff / count
print diff, avgDiff
diff = 0

for key in genes:
    diff += math.pow((genes[key] - avgDiff), 2)
sDiff = math.sqrt(diff / (count - 1))
print diff, sDiff

tcalc = avgDiff / sDiff * math.sqrt(count)

print tcalc

for key in sorted(genes):
    outfile.write(key + '\t' + str(genes[key]) + '\n')

print 'Finished!'
