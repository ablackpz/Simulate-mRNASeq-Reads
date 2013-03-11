import makeRandomTestData, os, random

genes = {}
name = '241rep1'
filename = 'DataSet' + name
numGenesMake = 5000
for i in range(0, numGenesMake):
    key = 'testgene_' + str(i) + ' '
    genes[key] = makeRandomTestData.makeKmerCountData(random.randint(101,4999), 'default')
errors  = 1

if makeRandomTestData.checkForFasta(filename + 'E1R100G100.fa'):
    x = os.remove(filename + 'E1R100G100.fa')
if makeRandomTestData.checkForFasta(filename + 'E1R100G100RandomReadsPair1.fa'):
    x = os.remove(filename + 'E1R100G100RandomReadsPair1.fa')
if makeRandomTestData.checkForFasta(filename + 'E1R100G100RandomReadsPair2.fa'):
    x = os.remove(filename + 'E1R100G100RandomReadsPair2.fa')

if makeRandomTestData.checkForFasta(filename + 'E1R100G100RandomReads.txt'):
    x = os.remove(filename + 'E1R100G100RandomReads.txt')

count = 0
count2 = 0
readLength = 100
insertSize = 50
coverage = 20
numGenes = len(genes)

for key in genes:
    thisGeneName = key
    if len(genes[thisGeneName]) > readLength:
        count2 += 1
        complete = makeRandomTestData.outputFastaSeq(filename + 'E1R100G100.fa', thisGeneName, genes[thisGeneName])
        complete = makeRandomTestData.makeRandomlyPlacedPairedEndReads(genes[thisGeneName], thisGeneName, readLength, insertSize, coverage, filename + 'E1R100G100RandomReadsPair1.fa', filename + 'E1R100G100RandomReadsPair2.fa', filename + 'E1R100G100RandomReads.txt', 1, 0)

        count += 1
    if count2 >= 5000:
        print count2
        break

print 'Finished'
