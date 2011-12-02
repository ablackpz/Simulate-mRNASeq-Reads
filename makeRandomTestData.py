import random, screed, aabpPyLib

def outputFastaSeq(filename, identifier, seq):
    outfile = open(filename, 'a')
    identifier = identifier.strip('>')
    outfile.write('>' + identifier + '\n')
    while len(seq) > 60:
        outfile.write(seq[0:60] + '\n')
        seq = seq[60:]
    outfile.write(seq + '\n')
    outfile.close()
    return 0

def inputFastaSeq(filename):
    fastas = {}
    for newString in open(filename):
        if newString[0] == '>':
            currId = newString.rstrip()
            currId = currId[1:]
            fastas[currId] = ''
        else:
            fastas[currId] = fastas[currId] + newString.rstrip()
    return fastas

def checkForFasta(filename):
    try: 
        infile = open(filename, 'r')
    except:
        return 0
    else:
        return 1

def outputGeneCoverage(filename, identifier, type, coverage):
    outfile = open(filename, 'a')
    outfile.write(identifier + '\t' + type + '\t' + str(coverage) + '\n')
    return 0

def countKmersSeq(seq, kLength):
    kmers = {}
    i = 0
    while i + kLength <= len(seq):
        newWord = seq[i:i + kLength]
        if kmers.has_key(newWord):
            kmers[newWord] += 1
        else:
            kmers[newWord] = 1
        i += 1
    return kmers

def countKmersFile(filename, kLength):
    kmers = {}
    fasta = {}
    identifier = 0
    fasta = inputFastaSeq(filename)
#    for newString in open(filename):
#        if newString[0] == '>':
#            identifier = newString.rstrip()
#        elif identifier:
#            newString = newString.rstrip()
#            fasta[identifier] = newString
#            lastIdentifier = identifier
#            identifier = 0
#        elif newString[0] == ('A' or 'C' or 'G' or 'T' or 'U' or 'N'):
#            newString = newString.rstrip()
#            fasta[lastIdentifier] = fasta[lastIdentifier] + newString
    for entry in fasta:        
            k = len(fasta[entry])
            i = 0
            while i + kLength <= k:
                newWord = fasta[entry][i:i + kLength]
                if kmers.has_key(newWord):
                    kmers[newWord] += 1
                elif kmers.has_key(aabpPyLib.reverseComplement(newWord, 'DNA')):
                    kmers[aabpPyLib.reverseComplement(newWord, 'DNA')] += 1
                else:
                    kmers[newWord] = 1
                i += 1
    
    return kmers

def makeKmerCountData(seqLength, alpha):
    data = ''
    if alpha == 'default':
        alphabet = {0:'A', 1:'C', 2:'G', 3:'T'}
        for i in range(0, seqLength):
            data = data + alphabet[random.randint(0, len(alphabet)-1)]
    elif alpha == 'chicken':
        data = makeChickenKmerCountData(seqLength)
    return data

def makeChickenKmerCountData(seqLength):
    data = ''
    alphabet = {0:'A', 1:'C', 2:'G', 3:'T'}
    for i in range(0, seqLength):
        newNucNum =random.randint(0, 100)
        if i % 3 == 0:
            if newNucNum in range(0, 22):
                newNuc = 'T'
            elif newNucNum in range(22, 45):
                newNuc = 'C'
            elif newNucNum in range(45, 75):
                newNuc = 'A'
            else:
                newNuc = 'G'
        elif i % 3 == 1:
            if newNucNum in range(0, 30):
                newNuc = 'T'
            elif newNucNum in range(30, 49):
                newNuc = 'C'
            elif newNucNum in range(49, 81):
                newNuc = 'A'
            else:
                newNuc = 'G'
        elif i % 3 == 2:
            if data[-2] == 'T' and data[-1] == 'T':
                if newNucNum in range(0, 32):
                    newNuc = 'T'
                elif newNucNum in range(32, 60):
                    newNuc = 'C'
                elif newNucNum in range(60, 80):
                    newNuc = 'A'
                else:
                    newNuc = 'G'
            elif data[-2] == 'T' and data[-1] == 'C':
                if newNucNum in range(0, 33):
                    newNuc = 'T'
                elif newNucNum in range(33, 66):
                    newNuc = 'C'
                elif newNucNum in range(66, 90):
                    newNuc = 'A'
                else:
                    newNuc = 'G'
            elif data[-2] == 'T' and data[-1] == 'A':
                if newNucNum in range(0, 53):
                    newNuc = 'T'
                elif newNucNum in range(53, 99):
                    newNuc = 'C'
                elif newNucNum in range(99, 100):
                    newNuc = 'A'
                else:
                    newNuc = 'G'
            elif data[-2] == 'T' and data[-1] == 'G':
                if newNucNum in range(0, 33):
                    newNuc = 'T'
                elif newNucNum in range(33, 74):
                    newNuc = 'C'
                else:
                    newNuc = 'G'
            elif data[-2] == 'C' and data[-1] == 'T':
                if newNucNum in range(0, 30):
                    newNuc = 'T'
                elif newNucNum in range(30, 44):
                    newNuc = 'C'
                elif newNucNum in range(44, 57):
                    newNuc = 'A'
                else:
                    newNuc = 'G'
            elif data[-2] == 'C' and data[-1] == 'C':
                if newNucNum in range(0, 36):
                    newNuc = 'T'
                elif newNucNum in range(36, 52):
                    newNuc = 'C'
                elif newNucNum in range(52, 91):
                    newNuc = 'A'
                else:
                    newNuc = 'G'
            elif data[-2] == 'C' and data[-1] == 'A':
                if newNucNum in range(0, 21):
                    newNuc = 'T'
                elif newNucNum in range(21, 37):
                    newNuc = 'C'
                elif newNucNum in range(37, 53):
                    newNuc = 'A'
                else:
                    newNuc = 'G'
            elif data[-2] == 'C' and data[-1] == 'G':
                if newNucNum in range(0, 30):
                    newNuc = 'T'
                elif newNucNum in range(30, 53):
                    newNuc = 'C'
                elif newNucNum in range(53, 71):
                    newNuc = 'A'
                else:
                    newNuc = 'G'
            elif data[-2] == 'A' and data[-1] == 'T':
                if newNucNum in range(0, 22):
                    newNuc = 'T'
                elif newNucNum in range(22, 50):
                    newNuc = 'C'
                elif newNucNum in range(50, 75):
                    newNuc = 'A'
                else:
                    newNuc = 'G'
            elif data[-2] == 'A' and data[-1] == 'C':
                if newNucNum in range(0, 43):
                    newNuc = 'T'
                elif newNucNum in range(43, 69):
                    newNuc = 'C'
                elif newNucNum in range(69, 88):
                    newNuc = 'A'
                else:
                    newNuc = 'G'
            elif data[-2] == 'A' and data[-1] == 'A':
                if newNucNum in range(0, 15):
                    newNuc = 'T'
                elif newNucNum in range(15, 33):
                    newNuc = 'C'
                elif newNucNum in range(33, 68):
                    newNuc = 'A'
                else:
                    newNuc = 'G'
            elif data[-2] == 'A' and data[-1] == 'G':
                if newNucNum in range(0, 18):
                    newNuc = 'T'
                elif newNucNum in range(18, 41):
                    newNuc = 'C'
                elif newNucNum in range(41, 68):
                    newNuc = 'A'
                else:
                    newNuc = 'G'
            elif data[-2] == 'G' and data[-1] == 'T':
                if newNucNum in range(0, 33):
                    newNuc = 'T'
                elif newNucNum in range(33, 49):
                    newNuc = 'C'
                elif newNucNum in range(49, 70):
                    newNuc = 'A'
                else:
                    newNuc = 'G'
            elif data[-2] == 'G' and data[-1] == 'C':
                if newNucNum in range(0, 28):
                    newNuc = 'T'
                elif newNucNum in range(28, 48):
                    newNuc = 'C'
                elif newNucNum in range(48, 92):
                    newNuc = 'A'
                else:
                    newNuc = 'G'
            elif data[-2] == 'G' and data[-1] == 'A':
                if newNucNum in range(0, 19):
                    newNuc = 'T'
                elif newNucNum in range(19, 31):
                    newNuc = 'C'
                elif newNucNum in range(31, 63):
                    newNuc = 'A'
                else:
                    newNuc = 'G'
            elif data[-2] == 'G' and data[-1] == 'G':
                if newNucNum in range(0, 33):
                    newNuc = 'T'
                elif newNucNum in range(33, 52):
                    newNuc = 'C'
                elif newNucNum in range(52, 73):
                    newNuc = 'A'
                else:
                    newNuc = 'G'
        else:
            print 'This should never print!'
        data = data + newNuc
    return data

def makeSingleKmerCountData(kLength, seqLength, Ns):
    data = ''
    if Ns:
        alphabet = {0:'A', 1:'C', 2:'G', 3:'T', 4:'N'}
    else:
        alphabet = {0:'A', 1:'C', 2:'G', 3:'T'}
    while len(data) < seqLength:
        if len(data) in range(0, kLength):
            data = data + alphabet[random.randint(0,len(alphabet)-1)]
        else:
            newNuc = alphabet[random.randint(0,len(alphabet)-1)]
            if data[-1 * kLength - 1: -1] + newNuc not in data and aabpPyLib.reverseComplement(data[-1 * kLength - 1: -1] + newNuc, 'DNA') not in data:
                data = data + newNuc
                print data[-1 * kLength: -1], len(data)
    return data

def makeSingleKmerPlusOneCountData(kLength, seqLength, repSeq, Ns):
    data = repSeq
    if Ns:
        alphabet = {0:'A', 1:'C', 2:'G', 3:'T', 4:'N'}
    else:
        alphabet = {0:'A', 1:'C', 2:'G', 3:'T'}
    while len(data) < seqLength:
        if len(data) in range(0, kLength):
            data = data + alphabet[random.randint(0, len(alphabet)-1)]
        else:
            newNuc = alphabet[random.randint(0, len(alphabet)-1)]
            if data[-1 * kLength -1: -1] + newNuc not in data or data[-1 * kLength -1: -1] + newNuc == repSeq:
                data = data + newNuc
    return data
    
def makeIsoform(kLength, seqLength, seqPortion, seqOriginal):
    data = seqOriginal
    alphabet = {0:'A', 1:'C', 2:'G', 3:'T'}
    while data == seqOriginal:
        data = seqPortion
        while len(data) < seqLength:
            if len(data) < seqLength:
                data = data + alphabet[random.randint(0, len(alphabet)-1)]
            else:
                newNuc = alphabet[random.randint(0, len(alphabet)-1)]
                if data[-1 * kLength -1: -1] + newNuc not in data:
                    data = data + newNuc
    return data

def addSeqErrors(read, errors):
    for errorCounter in range(0, len(read)):
        if random.randint(1, 101) <= errors:
            nuc = read[errorCounter]
#            print nuc
            if nuc == 'A':
                    seq = ['G', 'C', 'T']
            elif nuc == 'C':
                    seq = ['A', 'G', 'T']
            elif nuc == 'G':
                    seq = ['A', 'C', 'T']
            elif nuc == 'T':
                    seq = ['A', 'C', 'G']
            else:
                    seq = ['A', 'C', 'G', 'T']
            nuc = random.choice(seq)
            temp = read[:errorCounter] + nuc + read[errorCounter+1:]
            read = temp
#            print nuc
    return read

def addNs(seq, freq):
    for counter in range(0, len(seq)):
        if random.randint(1, 101) <= freq:
            temp = seq[:counter] + 'N' + seq[counter+1:]
            seq = temp
    return seq
            

def makeRandomlyPlacedReads(gene, identifier, readLength, numReads, filenameFasta, filenameCoverage, errors, Ns):
    coverageReq = len(gene) / readLength * numReads
    for i in range(0, coverageReq):
        if len(gene) >= readLength:
            position = random.randint(0,len(gene)-readLength)
            read = gene[position:position + readLength]
            if errors:
                read = addSeqErrors(read, errors)
            if Ns:
                read = addNs(read, Ns)
            identifier1 = identifier + 'Count' + str(i) + 'Begin' + str(position) + 'End' + str(position + readLength - 1)
            a = outputFastaSeq(filenameFasta, identifier1, read)
        else:
            pass
    b = outputGeneCoverage(filenameCoverage, identifier, 'Random Placement-Number of Reads' + ':' + str(coverageReq), numReads)
    return 1

def makeRandomlyPlacedPairedEndReads(gene, identifier, readLengthSide, insertSize, numReads, filenameFasta1, filenameFasta2, filenameCoverage, errors, Ns):
    totalReadLength = 2 * readLengthSide + insertSize
    coverageReq = len(gene) / totalReadLength * numReads
    for i in range(0, coverageReq):
        if len(gene) >= totalReadLength:
            position = random.randint(0,len(gene)-totalReadLength)
            read = gene[position:position + totalReadLength]
            if errors:
                read = addSeqErrors(read, errors)
            if Ns:
                read = addNs(read, Ns)
            identifier1 = identifier + 'Count' + str(i) + 'Begin' + str(position) + 'End' + str(position + (2 * readLengthSide) + insertSize - 1)
            a = outputFastaSeq(filenameFasta1, identifier1 + '\t1', read[:readLengthSide])
            identifier2 = identifier + 'Count' + str(i) + 'Begin' + str(position + readLengthSide + insertSize) + 'End' + str(position + (2 * readLengthSide) + insertSize - 1)
            a = outputFastaSeq(filenameFasta2, identifier1 + '\t2', read[-1*readLengthSide: -1])
        else:
            pass
    b = outputGeneCoverage(filenameCoverage, identifier, 'Random Placement-Number of Reads' + ':' + str(coverageReq), numReads)
    return 1


def makeUniformReads(gene, identifier, readLength, numReads, filenameFasta, filenameCoverage, errors, Ns):
    for i in range(0, numReads):
        position = 0
        while position + readLength <= len(gene):
            read = gene[position:position+readLength]
            identifier1 = identifier + 'Count' + str(i) + 'Begin' + str(position) + 'End' + str(position+readLength - 1)
            if errors:
                read = addSeqErrors(read, errors)
            if Ns:
                read = addNs(read, errors)
            a = outputFastaSeq(filenameFasta, identifier1, read)
            position += readLength
    b = outputGeneCoverage(filenameCoverage, identifier, 'Uniform Placement - Number of Passes', numReads)
    return 1

def makeUnevenReads(seq, identifier, readLength, numReads, skips, filenameFasta, filenameCoverage, errors, Ns):
#    print seq
    for i in range(0, numReads):
        position = random.randint(0, skips)
        while position + readLength <= len(seq):
            read = seq[position:position+readLength]
            identifier1 = identifier + 'Count' + str(i) + 'Begin' + str(position) + 'End' + str(position+readLength - 1)
            if errors:
                read = addSeqErrors(read, errors)
            if Ns:
                read = addNs(read, errors)
            a = outputFastaSeq(filenameFasta, identifier1, read)
            position = position + readLength + random.randint(0, skips)
    b = outputGeneCoverage(filenameCoverage, identifier, 'Uneven Placement - Number of Passes', numReads)
    return 1

