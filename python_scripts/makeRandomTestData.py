import random, os, aabpPyLib, time

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

def outputFastqSeq(filename, identifier, seq):
    outfile = open(filename, 'a')
    identifier = '@HWUSI-EAS1599:79:709W9AAXX:1:1:2039:936 1:N:0:GNCTAC'
    outfile.write(identifier + '\n')
    s = len(seq) + 1
    q = '#'*s
    outfile.write('N' + seq + '\n')
    outfile.write('+' + '\n')
    outfile.write(q + '\n')
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

def countKmersInitializedFile(filename, kLength, kmers):
    fasta = {}
    fasta = inputFastaSeq(filename)
    for entry in fasta:
        kmers = countKmersInitialized(fasta[entry], kLength, kmers)
    return kmers

def countKmersInitialized(seq, kLength, kmers):
    k = len(seq)
#    print seq
    i = 0
    while i + kLength <= k:
        newWord = seq[i:i + kLength]
#        print newWord
        if kmers.has_key(newWord):
            kmers[newWord] += 1
#            print 'Found key forward'
        elif kmers.has_key(aabpPyLib.reverseComplement(newWord, 'DNA')):
            kmers[aabpPyLib.reverseComplement(newWord, 'DNA')] += 1
#            print 'Found key reverse'
        else:
#            print 'Key should have been found, but was not'
            pass
        i += 1
    return kmers

def zeroInitializedDictionary(x):
    for key in x:
        x[key] = 0
    return x

def outputDictionaryContent(filename, x):
    outfile = open(filename, 'a')
    for key in sorted(x):
        outfile.write(key + '\t' + str(x[key]) + '\n')
    return len(x)

def outputDictionaryContentNoKey(filename, x):
    outfile = open(filename, 'a')
    for key in sorted(x):
        outfile.write(str(x[key]) + '\t')
    return len(x)

def inputDictionaryContent(filename, x):
    for newString in open(filename, 'r'):
        newString = newString.rstrip()
        parts = newString.split('\t')
        x[parts[0]] = parts[1]
    return x

def makeKmerCountData(seqLength, alpha):
    data = ''
    if alpha == 'default':
        alphabet = {0:'A', 1:'C', 2:'G', 3:'T'}
        for i in range(0, seqLength):
            data = data + alphabet[random.choice(range(0, 4))]
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
            if data[-1 * kLength -1: -1] + newNuc not in data and aabpPyLib.reverseComplement(data[-1 * kLength - 1: -1] + newNuc, 'DNA') not in data:
                data = data + newNuc
    return data

def makeAllOverlapReads(readLength, seq, identifier, outfile):
    seqLength = len(seq)
    print seqLength, readLength
    if seqLength < readLength:
        print 'flag'
        identifier1 = identifier + 'Begin0End' + str(seqLength - 1)
        complete = outputFastaSeq(outfile, identifier1, seq)
    else:
        for i in range(0, seqLength - readLength + 1):
            read = seq[i:i+readLength]
            identifier1 = identifier + 'Begin' + str(i) + 'End' + str(i + readLength - 1)
            complete = outputFastaSeq(outfile, identifier1, read)

    return 1
    
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
                if data[-1 * kLength -1: -1] + newNuc not in data and aabpPyLib.reverseComplement(data[-1 * kLength - 1: -1] + newNuc, 'DNA') not in data:
                    data = data + newNuc
    return data

def makeIsoformTruncation(identifier, seqOriginal, newLength, min, max):
    if len(seqOriginal) > min + 1:
        if newLength == 0:
            newLength = random.choice(range(1, len(seqOriginal) - min))
        seqNew = seqOriginal[0:len(seqOriginal) - newLength]
        identifierNew = identifier + '_Truncation_' + str(len(seqOriginal) - newLength)
    else:
        identifierNew = identifier
        seqNew = seqOriginal
    return identifierNew, seqNew

def makeIsoformExtension(identifier, seqOriginal, newLength, seqEnd, min, max):
    if len(seqOriginal) < max:
        if newLength == 0:
             newLength = random.randint(0, max - len(seqOriginal) - 1)
        if seqEnd == '':
             alphabet = {0:'A', 1:'C', 2:'G', 3:'T'}
             while len(seqEnd) < newLength:
                 seqEnd += alphabet[random.randint(0, len(alphabet)-1)]
        seqNew = seqOriginal + seqEnd
        identifierNew = identifier + '_Extension_' + str(len(seqEnd))
    else:
        identifierNew =identifier
        seqNew = seqOriginal
    return identifierNew, seqNew

def makeIsoformInsertion(identifier, seqOriginal, insertPosition, seqIn, min, max):
    if len(seqOriginal) < max - 1 and len(seqOriginal) > min:
        if insertPosition == -1:
             insertPosition = random.randint(1, len(seqOriginal) - 1)
        if len(seqIn) == 0:
             insertLength = random.randint(1, max - len(seqOriginal) - 1)
             alphabet = {0:'A', 1:'C', 2:'G', 3:'T'}
             while len(seqIn) < insertLength:
                 seqIn += alphabet[random.randint(0, len(alphabet)-1)]
        seqNew = seqOriginal[0:insertPosition] + seqIn + seqOriginal[insertPosition:len(seqOriginal)]
        identifierNew = identifier + '_Insertion_Pos_' + str(insertPosition) + '_Size_' + str(len(seqIn))
    else:
        identifierNew =identifier
        seqNew = seqOriginal
    return identifierNew, seqNew

def makeIsoformDeletion(identifier, seqOriginal, deletePosition, deleteLength, min, max):
    if len(seqOriginal) > min + 1:
        if deleteLength == 0:
             deleteLength = random.randint(1, len(seqOriginal) - min - 1)
        if deletePosition == -1:
             deletePosition = random.randint(0, len(seqOriginal) - deleteLength)
        seqNew = seqOriginal[0:deletePosition] + seqOriginal[deletePosition+deleteLength: len(seqOriginal)]
        identifierNew = identifier + '_Deletion_Pos_' + str(deletePosition) + '_Size_' + str(deleteLength)
    else:
        identifierNew =identifier
        seqNew = seqOriginal
    return identifierNew, seqNew

def makeIsoformSubstitution(identifier, seqOriginal, subPosition, seqSub, min, max):
    if len(seqOriginal) < max:
        if len(seqSub) == 0:
             subLength = random.randint(1, len(seqOriginal) - 1)
             alphabet = {0:'A', 1:'C', 2:'G', 3:'T'}
             while len(seqSub) < subLength:
                 seqSub += alphabet[random.randint(0, len(alphabet)-1)]
        subLength = len(seqSub)
        if subPosition == -1 and len(seqOriginal) > subLength:
             subPosition = random.randint(1, len(seqOriginal) - subLength)
        seqNew = seqOriginal[0:subPosition] + seqSub + seqOriginal[subPosition+subLength: len(seqOriginal)]
        identifierNew = identifier + '_Substitution_Pos_' + str(subPosition) + '_Size_' + str(len(seqSub))
    else:
        identifierNew =identifier
        seqNew = seqOriginal
    return identifierNew, seqNew

def makeIsoformSnps(identifier, seqOriginal, frequency):
    if frequency == 0:
        frequency = random.randint(1, 5)
    identifierNew = identifier + '_Snps_Freq_' + str(frequency)
    seqNew = addSeqErrors(seqOriginal, frequency)
    return identifierNew, seqNew

def generateIsoforms(identifier, seqOriginal, typeIsoform, option1, option2, option3, min, max):
    newSeq = seqOriginal
    while newSeq == seqOriginal:
        print identifier, len(seqOriginal)
        if typeIsoform == 'random':
            choice = -1
            if len(seqOriginal) < min + 2:
                choice = random.randint(1, 2)
            elif len(seqOriginal) > max - 2:
                choice = 0
            else:
#                options = {0:'truncation', 1:'extension', 2:'insertion', 3:'deletion', 4:'substitution', 5:'snps', 6:'truncationSnps', 7:'extensionSnps', 8:'insertionSnps', 9:'deletionSnps', 10:'substitutionSnps', 11:''}
                choice = random.randint(0, 4)
            if choice == 0:
                typeIsoform = 'truncation'
                option1 = 0
#            if choice == 1:
#                typeIsoform = 'truncationSnps'
#                option1 = 0
#                option3 = 0
            if choice == 1:
                typeIsoform = 'extension'
                option1 = 0
                option2 = ''
#            if choice == 3:
#                typeIsoform = 'extensionSnps'
#                option1 = 0
#                option2 = ''
#                option3 = 0
            if choice == 2:
                typeIsoform = 'insertion'
                option1 = -1
                option2 = ''
#            if choice == 5:
#                typeIsoform = 'insertionSnps'
#                option1 = -1
#                option2 = ''
#                option3 = 0
            if choice == 3:
                typeIsoform = 'deletion'
                option1 = -1
                option2 = 0
#            if choice == 7:
#                typeIsoform = 'deletionSnps'
#                option1 = -1
#                option2 = 0
#                option3 = 0
            if choice == 4:
                typeIsoform = 'substitution'
                option1 = -1
                option2 = ''
#            if choice == 9:
#                typeIsoform = 'substitutionSnps'
#                option1 = -1
#                option2 = ''
#                option3 = 0
#            if choice == 5:
#                typeIsoform = 'snps'
#                option3 = 0
        if typeIsoform == 'truncation':
             newId, newSeq = makeIsoformTruncation(identifier, seqOriginal, option1, min, max)
        if typeIsoform == 'truncationSnps':
             tmpId, tmpSeq = makeIsoformTruncation(identifier, seqOriginal, option1, min, max)
             newId, newSeq = makeIsoformSnps(tmpId, tmpSeq, option3)
        if typeIsoform == 'extension':
             newId, newSeq = makeIsoformExtension(identifier, seqOriginal, option1, option2, min, max)
        if typeIsoform == 'extensionSnps':
             tmpId, tmpSeq = makeIsoformExtension(identifier, seqOriginal, option1, option2, min, max)
             newId, newSeq = makeIsoformSnps(tmpId, tmpSeq, option3)
        if typeIsoform == 'insertion':
             newId, newSeq = makeIsoformInsertion(identifier, seqOriginal, option1, option2, min, max)
        if typeIsoform == 'insertionSnps':
             tmpId, tmpSeq = makeIsoformInsertion(identifier, seqOriginal, option1, option2, min, max)
             newId, newSeq = makeIsoformSnps(tmpId, tmpSeq, option3)
        if typeIsoform == 'deletion':
             newId, newSeq = makeIsoformDeletion(identifier, seqOriginal, option1, option2, min, max)
        if typeIsoform == 'deletionSnps':
             tmpId, tmpSeq = makeIsoformDeletion(identifier, seqOriginal, option1, option2, min, max)
             newId, newSeq = makeIsoformSnps(tmpId, tmpSeq, option3)
        if typeIsoform == 'substitution':
             newId, newSeq = makeIsoformSubstitution(identifier, seqOriginal, option1, option2, min, max)
        if typeIsoform == 'substitutionSnps':
             tmpId, tmpSeq = makeIsoformSubstitution(identifier, seqOriginal, option1, option2, min, max)
             newId, newSeq = makeIsoformSnps(tmpId, tmpSeq, option3)
        if typeIsoform == 'snps':
             newId, newSeq = makeIsoformSnps(identifier, seqOriginal, option3)
    if len(newSeq) > max or len(newSeq) < min:
        print 'PROBLEM!!!', newId
    return newId, newSeq

def addSeqErrors(read, errors):
    temp = ''
    for errorCounter in range(0, len(read)):
        if random.randint(1, 100) <= errors:
            seq= ['A', 'C', 'G', 'T']
            nuc = read[errorCounter]
            if nuc != 'N':
                seq.remove(nuc)
            nuc = random.choice(seq)
            temp += nuc
        else:
            temp += read[errorCounter]
    return temp

def addSeqErrorsId(read, identifier, errors):
    temp = ''
    for errorCounter in range(0, len(read)):
        if random.randint(1, 100) <= errors:
            seq= ['A', 'C', 'G', 'T']
            nuc = read[errorCounter]
            if nuc != 'N':
                seq.remove(nuc)
            nuc = random.choice(seq)
            temp += nuc
            identifier = identifier + '_' + str(errorCounter)
        else:
            temp += read[errorCounter]
    return temp, identifier

def addNs(seq, freq):
    for counter in range(0, len(seq)):
        if random.randint(1, 101) <= freq:
            temp = seq[:counter] + 'N' + seq[counter+1:]
            seq = temp
    return seq
            

def makeRandomlyPlacedReads(gene, identifier, readLength, numReads, filenameFasta, filenameCoverage, errors, Ns):
    coverageReq = float(len(gene)) / float(readLength) * float(numReads)
    if len(gene) >= readLength:
#        print coverageReq
        for i in range(0, int(coverageReq)):
#        if len(gene) >= readLength:
            position = random.randint(0,len(gene)-readLength)
            read = gene[position:position + readLength]
            identifier1 = identifier + 'Count' + str(i) + 'Begin' + str(position) + 'End' + str(position + readLength - 1)
            if errors:
                read, identifier1 = addSeqErrorsId(read, identifier1, errors)
            if Ns:
                read = addNs(read, Ns)
#            identifier1 = identifier + 'Count' + str(i) + 'Begin' + str(position) + 'End' + str(position + readLength - 1)
            a = outputFastaSeq(filenameFasta, identifier1, read)
    else:
        for i in range(0, int(coverageReq)):
            read = gene
            identifier1 = identifier + 'Count' + str(i) + 'Begin0End' + str(len(read)) 
            if errors:
                read, identifier1 = addSeqErrorsId(read, identifier1, errors)
            if Ns:
                read = addNs(read, Ns)
            a = outputFastaSeq(filenameFasta, identifier1, read)
    b = outputGeneCoverage(filenameCoverage, identifier, 'Random Placement - Number of Reads' + ':' + str(coverageReq), numReads)
    return 1

def makeRandomlyPlacedPairedEndReads(gene, identifier, readLengthSide, insertSize, numReads, filenameFasta1, filenameFasta2, filenameCoverage, errors, Ns):
    totalReadLength = 2 * readLengthSide + insertSize
    coverageReq = float(len(gene)) / float(totalReadLength) * float(numReads)
    if len(gene) >= totalReadLength:
        for i in range(0, int(coverageReq)):
#        if len(gene) >= totalReadLength:
            position = random.randint(0,len(gene)-totalReadLength)
#            print position, position + totalReadLength
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

#def makeUnevenReads(seq, identifier, readLength, numReads, skips, filenameFasta, filenameCoverage, errors, Ns):
#    print seq
#    for i in range(0, numReads):
#        position = random.randint(0, skips)
#        while position + readLength <= len(seq):
#            read = seq[position:position+readLength]
#            identifier1 = identifier + 'Count' + str(i) + 'Begin' + str(position) + 'End' + str(position+readLength - 1)
#            if errors:
#                read = addSeqErrors(read, errors)
#            if Ns:
#                read = addNs(read, errors)
#            a = outputFastaSeq(filenameFasta, identifier1, read)
#            position = position + readLength + random.randint(0, skips)
#    b = outputGeneCoverage(filenameCoverage, identifier, 'Uneven Placement - Number of Passes', numReads)
#    return 1

#def extractSimilarity(filename):
#    countLines = 0
#    countMatches = 0
#    for newString in open(filename):
#        if newString[0] != ' ':
##            print newString, countLines
#            countLines += 1
#            lastLine = newString.rstrip()
#        elif '*' in newString:
#            for c in newString:
#                if c == '*':
#                    countMatches += 1
#    lastLine = lastLine[20:].rstrip()
#    numChars = ((countLines / 2) - 1) * 60 + len(lastLine)
#
#    similarity = float(countMatches) / float(numChars) * 100
##    print countMatches, numChars, similarity
#    return similarity

#def callClustalw2(filenameSeq):
#    sts = os.system('/Applications/clustalw2 ' + '-INFILE=' + filenameSeq)
#    return 1

def createGroups(groups, id1, id2):
    size = len(groups)
    j = 0
    if size > 0:
        for i in range(0, size):
            if id1 in groups[i]:
                if id2 not in groups[i]:
                    groups[i].append(id2)
                j = 1
                break
            elif id2 in groups[i]:
                if id1 not in groups[i]:
                    groups[i].append(id1)
                j = 1
                break
        if j == 0:
            groups[size] = [id1, id2]

    else:
        groups[0] = [id1, id2]
    return groups

def recheckGroups(groups):
    if len(groups) > 0:
        for i in range(0, len(groups)):
            for j in range(i+1, len(groups)):
                for item in groups[j]:
                    if item in groups[i]:
                        for item2 in groups[j]:
                            if item2 not in groups[i]:
                                groups[i].append(item2)
                        groups[j] = []
                        break
#        i = 0
#        while i < len(groups):
#            if groups[i] == []:
#                groups.pop(i)
#            i += 1
    return groups

def generateGroupsBowtie(groups, filename):
    count = 0
    for newString in open(filename):
        newString = newString.rstrip()
        ids = newString.split(' ')
#        if ids[0] < ids[1]:
#            ids1 = ids[1]
#            ids2 = ids[0]
#        else:
#            ids1 = ids[0]
#            ids2 = ids[1]
        groups = createGroups(groups, ids[0], ids[1])
        count += 1
        if not count % 1000:
            print 'Record ', count
    groups = recheckGroups(groups)
    groups = recheckGroups(groups)
    i = 0
    while i < len(groups):
        if groups[i] == []:
            groups.pop(i)
        i += 1
    return groups

def restoreIdentifiers(groups, seqs):
    ids = {}
    for id in seqs:
        shortId = id.split(' ')
        ids[shortId[0]] = id
    for key in groups:
        num = len(groups[key])
        for item in range(0, num):
            groups[key][item] = findIdentifier(groups[key][item], ids)
    return groups

def restoreIdentifiersEnsembl(groups, seqs):
    for key in groups:
        num = len(groups[key])
        for item in range(0, num):
            groups[key][item] = findIdentifier(groups[key][item], seqs)
    return groups

def findIdentifier(id, idList):
    if id in idList.keys():
        identifier = idList[id]
    else:
        identifier = id
    return identifier

def findGeneExpressionFromTranscripts(groups, infileMap):
    geneExp = {}
    for key in groups:
        geneExp[key] = 0
    count = 0
    for newString in open(infileMap):
        newString = newString.rstrip()
        count = count + 1
        if not count % 1000:
            print 'Record ', count
        for key in groups:
            if newString in groups[key]:
                geneExp[key] = geneExp[key] + 1
                break
    return geneExp

def findGeneExpressionFromTranscripts2(groups, infileMap):
    geneExp = {}
#    for key in groups:
#        geneExp[key] = 0
    count = 0
    notFound = 0
    for newString in open(infileMap):
        newString = newString.rstrip()
        count = count + 1
        if not count % 1000:
            print 'Record ', count
        if groups.has_key(newString):    
            if geneExp.has_key(groups[newString]):
                geneExp[groups[newString]] += 1
            else:
                geneExp[groups[newString]] = 1
        else:
            notFound += 1
#        for key in groups:
#            if newString in groups[key]:
#                geneExp[key] = geneExp[key] + 1
#                break
    print 'IDs not found ', notFound

    return geneExp

def outputSimilarGroups(groups, filename):
    outfile = open(filename, 'w')
    for key in groups:
        outfile.write(str(key) + '\t' + str(groups[key]) + '\n')

    outfile.close()
    return 1

def outputSimilarGroupsOneToOne(groups, filename):
    outfile = open(filename, 'w')
    for key in groups:
        outfile.write(str(key) + '\t' + str(key) + '\n')
        if len(groups[key]) >= 1:
            for item in groups[key]:
                outfile.write(str(item) + '\t' + str(key) + '\n')
    outfile.close()
    return 1

def inputSimilarGroups(groups, filename):
    for newString in open(filename):
        newString = newString.rstrip()
        parts = newString.split('\t')
        groups[parts[0]] = parts[1]
    return groups

def inputSimilarGroupsSpaceDelim(groups, filename):
    for newString in open(filename):
        newString = newString.rstrip()
        parts = newString.split(' ')
        groups[parts[0]] = parts[1]
    return groups

def reassignSimilarGroupKeys(groups):
    tmp = {}
    for key in groups:
        newKey = groups[key][0]
        newList = []
        for item in groups[key]:
            if item != newKey:
                newList.append(item)
        tmp[newKey] = newList
    return tmp

def countSimilarGroupsHistogram(groups, filename):
    outfile = open(filename, 'w')
    for key in groups:
        outfile.write(str(key) + '\t' + str(len(groups[key])) + '\n')
    outfile.close()
    return 1
