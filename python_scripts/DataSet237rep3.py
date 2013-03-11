import makeRandomTestData, os, random

genes = {}
name = '237rep3'
#infileName = 'Mus_musculus.NCBIM37.65.cdna.all.fa'
filename = 'DataSet' + name
#genes = makeRandomTestData.inputFastaSeq(infileName)
numGenesMake = 5000
for i in range(0, numGenesMake):
    key = 'testgene_' + str(i) + ' '
    genes[key] = makeRandomTestData.makeKmerCountData(random.randint(101,4999), 'default')
errors  = 1

if makeRandomTestData.checkForFasta(filename + 'E1R100G100.fa'):
    x = os.remove(filename + 'E1R100G100.fa')
if makeRandomTestData.checkForFasta(filename + 'E1R100G100RandomReads.fa'):
    x = os.remove(filename + 'E1R100G100RandomReads.fa')
if makeRandomTestData.checkForFasta(filename + 'E1R100G100RandomReads.txt'):
    x = os.remove(filename + 'E1R100G100RandomReads.txt')

count = 0
count2 = 0
readLength = 100
numGenes = len(genes)

for key in genes:
    thisGeneName = key
    if len(genes[thisGeneName]) > readLength:
        count2 += 1
        complete = makeRandomTestData.outputFastaSeq(filename + 'E1R100G100.fa', thisGeneName, genes[thisGeneName])
#        levelKey = random.randint(0, 5)
#        if levelKey == 0:
#            level = 10
#        elif levelKey == 1:
#            level = 100
#        elif levelKey == 2:
#            level = 1000
#        else:
#            level = 0
        level = 20
        coverageReq = float(len(genes[thisGeneName])) / float(readLength) * float(level)
        for i in range(0, int(coverageReq)):
            position = random.randint(0,len(genes[thisGeneName])-readLength)
            read = genes[thisGeneName][position:position + readLength]
            identifier1 = key + 'Count' + str(i) + 'Begin' + str(position) + 'End' + str(position + readLength - 1)
            if errors:
                read, identifier1 = makeRandomTestData.addSeqErrorsId(read, identifier1, errors)

            a = makeRandomTestData.outputFastaSeq(filename + 'E1R100G100RandomReads.fa', identifier1, read)
        b = makeRandomTestData.outputGeneCoverage(filename + 'E1R100G100RandomReads.txt', key, 'Random Placement - Number of Reads' + ':' + str(coverageReq), level)

        count += 1
    if count2 >= 5000:
        print count2
        break

print 'Finished'
