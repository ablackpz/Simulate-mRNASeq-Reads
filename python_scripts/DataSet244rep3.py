import makeRandomTestData, os, random

genes = {}
name = '244rep3'
infileName = 'Gallus_gallus.WASHUC2.63.cdna.all.fa'
filename = 'DataSet' + name
genes = makeRandomTestData.inputFastaSeq(infileName)
errors  = 1

if makeRandomTestData.checkForFasta(filename + 'E1R100G100.fa'):
    x = os.remove(filename + 'E1R100G100.fa')
if makeRandomTestData.checkForFasta(filename + 'E1R100G100RandomReadsPair1.fa'):
    x = os.remove(filename + 'E1R100G100RandomReadsPair1.fa')
if makeRandomTestData.checkForFasta(filename + 'E1R100G100RandomReadsPair2.fa'):
    x = os.remove(filename + 'E1R100G100RandomReadsPair2.fa')
if makeRandomTestData.checkForFasta(filename + 'E1R100G100RandomReads.txt'):
    x = os.remove(filename + 'E1R100G100RandomReads.txt')
if makeRandomTestData.checkForFasta(filename + 'E1R90G100.fa'):
    x = os.remove(filename + 'E1R90G100.fa')
if makeRandomTestData.checkForFasta(filename + 'E1R80G100.fa'):
    x = os.remove(filename + 'E1R80G100.fa')
if makeRandomTestData.checkForFasta(filename + 'E1R70G100.fa'):
    x = os.remove(filename + 'E1R70G100.fa')
if makeRandomTestData.checkForFasta(filename + 'E1R60G100.fa'):
    x = os.remove(filename + 'E1R60G100.fa')
if makeRandomTestData.checkForFasta(filename + 'E1R50G100.fa'):
    x = os.remove(filename + 'E1R50G100.fa')
if makeRandomTestData.checkForFasta(filename + 'E1R40G100.fa'):
    x = os.remove(filename + 'E1R40G100.fa')
if makeRandomTestData.checkForFasta(filename + 'E1R30G100.fa'):
    x = os.remove(filename + 'E1R30G100.fa')
if makeRandomTestData.checkForFasta(filename + 'E1R20G100.fa'):
    x = os.remove(filename + 'E1R20G100.fa')
if makeRandomTestData.checkForFasta(filename + 'E1R10G100.fa'):
    x = os.remove(filename + 'E1R10G100.fa')



count = 0
readLength = 100
insertSize = 50
totalReadLength = readLength * 2 + insertSize
numGenes = len(genes)
r90 = int(numGenes * .9)
r80 = int(numGenes * .8)
r70 = int(numGenes * .7)
r60 = int(numGenes * .6)
r50 = int(numGenes * .5)
r40 = int(numGenes * .4)
r30 = int(numGenes * .3)
r20 = int(numGenes * .2)
r10 = int(numGenes * .1)

for key in genes:
    thisGeneName = key
    if len(genes[thisGeneName]) > totalReadLength:
        complete = makeRandomTestData.outputFastaSeq(filename + 'E1R100G100.fa', thisGeneName, genes[thisGeneName])
        levelKey = random.randint(0, 3)
        if levelKey == 0:
            level = 10
        elif levelKey == 1:
            level = 100
        elif levelKey == 2:
            level = 1000
        else:
            level = 0

        complete = makeRandomTestData.makeRandomlyPlacedPairedEndReads(genes[thisGeneName], thisGeneName, readLength, insertSize, level, filename + 'E1R100G100RandomReadsPair1.fa', filename + 'E1R100G100RandomReadsPair2.fa', filename + 'E1R100G100RandomReads.txt', 1, 0)

        count += 1

genes2 = makeRandomTestData.inputFastaSeq(infileName)
for i in range(0, r90):
    thisGeneName = random.choice(genes2.keys())
    complete = makeRandomTestData.outputFastaSeq(filename + 'E1R90G100.fa', thisGeneName, genes2[thisGeneName])
    genes2.pop(thisGeneName)

genes2 = makeRandomTestData.inputFastaSeq(infileName)
for i in range(0, r80):
    thisGeneName = random.choice(genes2.keys())
    complete = makeRandomTestData.outputFastaSeq(filename + 'E1R80G100.fa', thisGeneName, genes2[thisGeneName])
    genes2.pop(thisGeneName)

genes2 = makeRandomTestData.inputFastaSeq(infileName)
for i in range(0, r70):
    thisGeneName = random.choice(genes2.keys())
    complete = makeRandomTestData.outputFastaSeq(filename + 'E1R70G100.fa', thisGeneName, genes2[thisGeneName])
    genes2.pop(thisGeneName)

genes2 = makeRandomTestData.inputFastaSeq(infileName)
for i in range(0, r60):
    thisGeneName = random.choice(genes2.keys())
    complete = makeRandomTestData.outputFastaSeq(filename + 'E1R60G100.fa', thisGeneName, genes2[thisGeneName])
    genes2.pop(thisGeneName)

genes2 = makeRandomTestData.inputFastaSeq(infileName)
for i in range(0, r50):
    thisGeneName = random.choice(genes2.keys())
    complete = makeRandomTestData.outputFastaSeq(filename + 'E1R50G100.fa', thisGeneName, genes2[thisGeneName])
    genes2.pop(thisGeneName)

genes2 = makeRandomTestData.inputFastaSeq(infileName)
for i in range(0, r40):
    thisGeneName = random.choice(genes2.keys())
    complete = makeRandomTestData.outputFastaSeq(filename + 'E1R40G100.fa', thisGeneName, genes2[thisGeneName])
    genes2.pop(thisGeneName)

genes2 = makeRandomTestData.inputFastaSeq(infileName)
for i in range(0, r30):
    thisGeneName = random.choice(genes2.keys())
    complete = makeRandomTestData.outputFastaSeq(filename + 'E1R30G100.fa', thisGeneName, genes2[thisGeneName])
    genes2.pop(thisGeneName)

genes2 = makeRandomTestData.inputFastaSeq(infileName)
for i in range(0, r20):
    thisGeneName = random.choice(genes2.keys())
    complete = makeRandomTestData.outputFastaSeq(filename + 'E1R20G100.fa', thisGeneName, genes2[thisGeneName])
    genes2.pop(thisGeneName)

genes2 = makeRandomTestData.inputFastaSeq(infileName)
for i in range(0, r10):
    thisGeneName = random.choice(genes2.keys())
    complete = makeRandomTestData.outputFastaSeq(filename + 'E1R10G100.fa', thisGeneName, genes2[thisGeneName])
    genes2.pop(thisGeneName)





print 'Finished'
