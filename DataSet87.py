import makeRandomTestData, os, random

repSeq = makeRandomTestData.makeSingleKmerCountData(32, 32, 0)
gene = makeRandomTestData.makeSingleKmerPlusOneCountData(32, 1000, repSeq, 0)
filename = 'DataSet87'
geneName = 'test_gene'
if makeRandomTestData.checkForFasta(filename + '.fa'):
    outfile = open(filename + '.fa', 'w')
    outfile.close()
    outfile = open(filename + 'Reads.fa', 'w')
    outfile.close()
    outfile = open(filename + 'Reads.txt', 'w')
    outfile.close()
genes = {}
for i in range(0, 10):
    thisGeneName = geneName + '_' + str(i)
    genes[thisGeneName] = makeRandomTestData.addSeqErrors(gene, 10)
    complete = makeRandomTestData.outputFastaSeq(filename + '.fa', thisGeneName, genes[thisGeneName])
    complete = makeRandomTestData.makeRandomlyPlacedReads(genes[thisGeneName], thisGeneName, 100, 50, filename + 'Reads.fa', filename + 'Reads.txt', 1, 0) 
