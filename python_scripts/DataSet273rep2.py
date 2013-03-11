import makeRandomTestData, os, random

genes = {}
name = '273rep2'
infileName = 'Mus_musculus.NCBIM37.65.cdna.all.fa'
filename = 'DataSet' + name
genes = makeRandomTestData.inputFastaSeq(infileName)
errors  = 0

if makeRandomTestData.checkForFasta(filename + 'E1R100G100.fa'):
    x = os.remove(filename + 'E1R100G100.fa')
if makeRandomTestData.checkForFasta(filename + 'E1R100G100RandomReadsPair1.fa'):
    x = os.remove(filename + 'E1R100G100RandomReadsPair1.fa')
if makeRandomTestData.checkForFasta(filename + 'E1R100G100RandomReadsPair2.fa'):
    x = os.remove(filename + 'E1R100G100RandomReadsPair2.fa')
if makeRandomTestData.checkForFasta(filename + 'E1R100G100RandomReads.txt'):
    x = os.remove(filename + 'E1R100G100RandomReads.txt')

count = 0
readLength = 300
insertSize = 400
totalReadLength = readLength * 2 + insertSize
numGenes = len(genes)

for key in genes:
    thisGeneName = key
    if len(genes[thisGeneName]) > totalReadLength:
        complete = makeRandomTestData.outputFastaSeq(filename + 'E1R100G100.fa', thisGeneName, genes[thisGeneName])
        level = 20

        complete = makeRandomTestData.makeRandomlyPlacedPairedEndReads(genes[thisGeneName], thisGeneName, readLength, insertSize, level, filename + 'E1R100G100RandomReadsPair1.fa', filename + 'E1R100G100RandomReadsPair2.fa', filename + 'E1R100G100RandomReads.txt', errors, 0)

        count += 1

print 'Finished'
