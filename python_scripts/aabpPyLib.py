import math


def reverseComplement(string,nuc):
    if nuc == 'DNA':
        alpha = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    elif nuc == 'RNA':
        alpha = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A'}
    reversed = ''
    for char in string:
        reversed = alpha.get(char, 'N') + reversed
    return reversed

def findMedian(medianList):
    medianList.sort()
    length = len(medianList)
    if length % 2 == 1:
        median = medianList[((length + 1) / 2 - 1)]
    else:
        lower = medianList[length / 2 - 1]
        upper = medianList[length / 2]
        median = (float(upper + lower)) / 2

    return median

def findLowestQuartile(medianList):
    medianList.sort()
    length = len(medianList)
    newLength = length // 4
    return medianList[0:newLength]

def meanStdDev(medianList):
    n, mean, std = len(medianList), 0, 0
    for i in medianList:
        mean = mean + i
    mean = mean / float (n)
    for a in medianList:
        std = std + (i - mean)**2
    std = math.sqrt(std / float(n - 1))
    return mean, std
        
def convertDecimaltoQuaternary(x):
    lengthDec = len(str(x))
    n = x
    r = ''
    while n > 4:
        q = n / 4
        r1 = n % 4
        r = str(r1) + r
        n = q
        print q, r1
    r1 = n % 4
    r = str(r1) + r
    quaternary = int(r)
    return quaternary

def convertQuaternarytoDecimal(x):
    n = str(x)
    sum = 0
    for i in range(0, len(n)):
        interim = int(n[-i - 1]) * 4**i
        sum += interim
#        print i, n[-i], interim
    return sum

def convertQuaternarytoDna(x, length):
    n = str(x)
    while len(n) < length:
        n = '0' + n
    n = n.replace('0', 'A')
    n = n.replace('1', 'C')
    n = n.replace('2', 'G')
    n = n.replace('3', 'T')
    return n

def convertDnatoQuaternary(x):
    n = x
    n = n.replace('A', '0')
    n = n.replace('C', '1')
    n = n.replace('G', '2')
    n = n.replace('T', '3')
    return int(n)
