import makeRandomTestData, os, random


infileName = 'Gallus_gallus.WASHUC2.63.cdna.all.fa'
genes = makeRandomTestData.inputFastaSeq(infileName)
filename = 'DataSet130'
if makeRandomTestData.checkForFasta(filename + '.fa'):
    outfile = open(filename + '.fa', 'w')
    outfile.close()
    outfile = open(filename + 'Reads.fa', 'w')
    outfile.close()
    outfile = open(filename + 'Reads.txt', 'w')
    outfile.close()
for thisGeneName in genes:
    complete = makeRandomTestData.outputFastaSeq(filename + '.fa', thisGeneName, genes[thisGeneName])
    complete = makeRandomTestData.makeRandomlyPlacedReads(genes[thisGeneName], thisGeneName, 100, 10, filename + 'Reads.fa', filename + 'Reads.txt', 0, 0) 
