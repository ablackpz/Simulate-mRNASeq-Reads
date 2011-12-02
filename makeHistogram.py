# A script to take a single column of data and make histogram type data for R - when there is too much data for R to handle
# 2011.11.10
# A. Black P.

# Usage: python makeHistogram.py input.txt minBin maxBin binSize output.txt

import sys

maxBin = float(sys.argv[3])
minBin = float(sys.argv[2])
binSize = float(sys.argv[4])
bins = {}

outfile = open(sys.argv[5], 'w')

startkey = minBin

while startkey < maxBin:
    bins[startkey] = 0
    startkey += binSize

print 'Loading/counting data\n'

count = 0
sum = 0
count2 = 0

for newString in open(sys.argv[1]):
    data = float(newString.rstrip())
    sum += data
#    print data
    for key in sorted(bins):
        if key <= data < key + binSize:
            bins[key] += 1
            count2 += 1
#            print data
    count += 1

for key in sorted(bins):
    outfile.write(str(key + 0.5 * binSize) + '\t' + str(bins[key]) + '\n')
print 'Average: ', sum / count

print >> sys.stderr, count, count2
print >> sys.stderr, 'Finished!'
