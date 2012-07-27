# A script to calculate median windows from a count-median-expr-all output file from khmer
# Original: 2011.12.07
# Original: A. Black P.
# Last modified: 2011.12.07
# Last modified: A. Black P.

# Usage: python calcMedianWindows.py input.out.all k output.out.windows

import sys, aabpPyLib

print 'Loading data\n'

count = 0
entries = {}
k = int(sys.argv[2])

for entry in open(sys.argv[1]):
    if entry[0] == '>':
        key = entry.rstrip()
        entries[key] = []
    else:
        entry = entry.rstrip()
        entry = entry.strip('[')
        entry = entry.strip(']')
        seq = entry.split(', ')
        size = len(seq)
        temp = []
        last = seq[size-1].split(']')
        seq[size-1] = last[0]
#        print seq[size-1]
        for i in range(0, size):
#            print temp
            temp.append(int(seq[i]))
#        print temp
        entries[key] = temp

for key in entries:
#    print len(entries[key])
    name = key.split(' ')
    i = 0
    allMed = []
    while i < len(entries[key]) - k:
#    for i in range(0, len(entries[key]) - k, k):
        seq = entries[key]
        frag = seq[i:i+k]
#        print i, i+k, frag, len(frag)
        med = aabpPyLib.findMedian(frag)
        mean, std = aabpPyLib.meanStdDev(frag)
        print name[0], med, std
        allMed.append(med)
        i += k
    mean, std = aabpPyLib.meanStdDev(allMed)
    print name[0], aabpPyLib.findMedian(aabpPyLib.findLowestQuartile(allMed))


#print entries


print 'Finished!'
