# A script to take a column of numbers and calc the mean and stdev
# 2011.12.01
# A. Black P.

# Usage: python getStdDev.py input.txt

import sys, math

print 'Loading/counting data\n'

count = 0
sum = 0
count2 = 0

for newString in open(sys.argv[1]):
    data = float(newString.rstrip())
    sum += data
    count += 1
avg = sum / count

sum = 0
for newString in open(sys.argv[1]):
    data = float(newString.rstrip())
    sum += math.pow(data - avg, 2)
stddev = math.sqrt(sum / (count))

print 'Average: ', avg, 'Std Dev: ', stddev

#print >> sys.stderr, count
print >> sys.stderr, 'Finished!'
