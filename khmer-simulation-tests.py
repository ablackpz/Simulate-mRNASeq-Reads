import makeRandomTestData, os, random


#Test 1: correctly output a fasta file
data1 = 'ACACACACACACACACACAGAGAGAGAGAGAGAGAGAGAGAGAGAGAGAGAGAGAGAGAGAG'
complete = makeRandomTestData.outputFastaSeq('Test1.fa', 'test_gene', data1)
fastas = makeRandomTestData.inputFastaSeq('Test1.fa')
for key in fastas.keys():
    myKey = key
if fastas[myKey] == data1:
    print 'Passed Test1.1\n'
else:
    print 'Failed Test1.1\n'
data2 = 'TATATATATATATATATATATATATATATATATATATATATATATATATATATATATATATA'
complete = makeRandomTestData.outputFastaSeq('Test1.fa', 'test_gene2', data2)
fastas = makeRandomTestData.inputFastaSeq('Test1.fa')
success = 0
for key in fastas.keys():
    if fastas[key] == data1 or fastas[key] == data2:
        pass
    else:
        success += 1
if success == 0:
    print 'Passed Test1.2\n'
else:
    print 'Failed Test1.2\n'

#Test 2: lk for fasta file before attempting to use it
success = makeRandomTestData.checkForFasta('Test1.fa')
if success:
    print 'Passed Test2.1\n'
else:
    print 'Failed Test2.1\n'
success = makeRandomTestData.checkForFasta('IDoNoExist.fa')
if success:
    print 'Failed Test2.2\n'
else:
    print 'Passed Test2.2\n'

#Test 3: make gene with all unique kmers
gene = makeRandomTestData.makeSingleKmerCountData(32, 1000, 0)
kmers = makeRandomTestData.countKmersSeq(gene, 32)
count = 0
for key in kmers:
    if kmers[key] > 1:
        count += 1
if count > 0:
    print 'Failed Test3.1\n'
else:
    print 'Passed Test3.1\n'
gene = makeRandomTestData.makeSingleKmerCountData(32, 1000, 1)
kmers = makeRandomTestData.countKmersSeq(gene, 32)
count = 0
for key in kmers:
    if kmers[key] > 1:
        count += 1
if count == 0 and 'N' in gene:
    print 'Passed Test3.2\n'
else:
    print 'Failed Test3.2\n'

#Test 4: make gene with unique kmers except for one repetitive seq
repSeq = 'A' * 32
gene = makeRandomTestData.makeSingleKmerPlusOneCountData(32, 1000, repSeq, 0)
kmers = makeRandomTestData.countKmersSeq(gene, 32)
count = 0
reps = 0
for key in kmers:
    if kmers[key] > 1 and key != repSeq:
        count += 1
    if key == repSeq:
        reps += 1
if count == 0 and reps > 0:
    print 'Passed Test4.1\n'
#    print reps
else:
    print 'Failed Test4.1\n'
#    print count, reps
#    print gene

#Test 5: make isoform with unique kmers
gene = makeRandomTestData.makeSingleKmerCountData(32, 1000, 0)
genePortion = gene[0:random.randint(1, len(gene))]
isoform = makeRandomTestData.makeIsoform(32, 1000, genePortion, gene)
if genePortion in isoform and isoform != gene:
    print 'Passed Test5.0\n'
else:
    print 'Failed Test5.0\n'

#Test 6: make simple reads for a simulated gene
gene = makeRandomTestData.makeSingleKmerCountData(32, 1000, 0)
if makeRandomTestData.checkForFasta('Test6.fa'):
    outfile = open('Test6.fa', 'w')
    outfile.close()
    outfile = open('Test6.txt', 'w')
    outfile.close()
complete = makeRandomTestData.makeRandomlyPlacedReads(gene, 'test_gene', 61, 1, 'Test6.fa', 'Test6.txt', 0, 0)
readBack = makeRandomTestData.inputFastaSeq('Test6.fa')
for key in readBack.keys():
    myKey = key
if readBack[myKey] in gene:
    success1 = 1
else:
    success1 = 0
infile = open('Test6.txt','r')
newString = infile.readline()
parts = newString.split('\t')
parts[2] = parts[2].rstrip()
if parts[2] == '1':
    success2 = 1
else:
    success2 = 0
if success1 and success2:
    print 'Passed Test6.0\n'
else:
    print 'Failed Test6.0\n'
outfile = open('Test6.fa', 'w')
outfile.close()
outfile = open('Test6.txt', 'w')
outfile.close()
complete = makeRandomTestData.makeRandomlyPlacedReads(gene, 'test_gene', 200, 1, 'Test6.fa', 'Test6.txt', 5, 0)
readBack = makeRandomTestData.inputFastaSeq('Test6.fa')
for key in readBack.keys():
    myKey = key
if readBack[myKey] not in gene:
    success1 = 1
else:
    success1 = 0
infile = open('Test6.txt','r')
newString = infile.readline()
parts = newString.split('\t')
parts[2] = parts[2].rstrip()
if parts[2] == '1':
    success2 = 1
else:
    success2 = 0
if success1 and success2:
    print 'Passed Test6.1\n'
else:
    print 'Failed Test6.1', success1, success2, gene, parts

# Test 7: add N's to a read
gene = makeRandomTestData.makeSingleKmerCountData(32, 1000, 0)
if makeRandomTestData.checkForFasta('Test7.fa'):
    outfile = open('Test7.fa','w')
    outfile.close()
    outfile = open('Test7.txt', 'w')
    outfile.close()
complete = makeRandomTestData.makeRandomlyPlacedReads(gene, 'test_gene', 200, 1, 'Test7.fa', 'Test7.txt', 0, 5)
readBack = makeRandomTestData.inputFastaSeq('Test7.fa')
for key in readBack.keys():
    myKey = key
if readBack[myKey] not in gene and 'N' in readBack[myKey]:
    success1 = 1
else:
    success1 = 0
infile = open('Test7.txt','r')
newString = infile.readline()
parts = newString.split('\t')
parts[2] = parts[2].rstrip()
if parts[2] == '1':
    success2 = 1
else:
    success2 = 0
if success1 and success2:
    print 'Passed Test7.0\n'
else:
    print 'Failed Test7.0', success1, success2, gene, parts

# Test 8: make uniform reads
gene = makeRandomTestData.makeSingleKmerCountData(32, 1000, 0)
if makeRandomTestData.checkForFasta('Test8.fa'):
    outfile = open('Test8.fa', 'w')
    outfile.close()
    outfile = open('Test8.txt', 'w')
    outfile.close()
complete = makeRandomTestData.makeUniformReads(gene, 'test_gene', 100, 1, 'Test8.fa', 'Test8.txt', 0, 0)
readBack = makeRandomTestData.inputFastaSeq('Test8.fa')
count = 0
for key in readBack.keys():
    count += 1
    if readBack[key] in gene:
        success1 = 0
    else:
        success1 = 1
if count == 10 and success1 == 0:
    print 'Passed Test8.0\n'
else:
    print 'Failed Test8.0\n'
if makeRandomTestData.checkForFasta('Test8.fa'):
    outfile = open('Test8.fa', 'w')
    outfile.close()
    outfile = open('Test8.txt', 'w')
    outfile.close()
complete = makeRandomTestData.makeUniformReads(gene, 'test_gene', 100, 1, 'Test\
8.fa', 'Test8.txt', 1, 0)
readBack = makeRandomTestData.inputFastaSeq('Test8.fa')
#print gene
count = 0
for key in readBack.keys():
    count += 1
if count == 10:
    print 'Passed Test8.1\n'
else:
    print 'Failed Test8.1\n'

# Test 9: make uniform reads                                                   
gene = makeRandomTestData.makeSingleKmerCountData(32, 1000, 0)
if makeRandomTestData.checkForFasta('Test9.fa'):
    outfile = open('Test9.fa', 'w')
    outfile.close()
    outfile = open('Test9.txt', 'w')
    outfile.close()
complete = makeRandomTestData.makeUnevenReads(gene, 'test_gene', 100, 1, 0,'Test9.fa', 'Test9.txt', 0, 0)
readBack = makeRandomTestData.inputFastaSeq('Test9.fa')
count = 0
for key in readBack.keys():
    count += 1
    if readBack[key] in gene:
        success1 = 1
    else:
        success1 = 0
if count == 10 and success1:
    print 'Passed Test9.0\n'
else:
    print 'Failed Test9.0\n'
    print count, success1
if makeRandomTestData.checkForFasta('Test9.fa'):
    outfile = open('Test9.fa', 'w')
    outfile.close()
    outfile = open('Test9.txt', 'w')
    outfile.close()
complete = makeRandomTestData.makeUnevenReads(gene, 'test_gene', 100, 1, 1,'Test9.fa', 'Test9.txt', 0, 0)
readBack = makeRandomTestData.inputFastaSeq('Test9.fa')
count = 0
for key in readBack.keys():
    count += 1
    if readBack[key] in gene:
        success1 = 1
    else:
        success1 = 0
if count >= 9 and success1:
    print 'Passed Test9.1\n'
else:
    print 'Failed Test9.1\n'
    print count, success1
if makeRandomTestData.checkForFasta('Test9.fa'):
    outfile = open('Test9.fa', 'w')
    outfile.close()
    outfile = open('Test9.txt', 'w')
    outfile.close()
complete = makeRandomTestData.makeUnevenReads(gene, 'test_gene', 100, 1, 1,'Test9.fa', 'Test9.txt', 1, 0)
readBack = makeRandomTestData.inputFastaSeq('Test9.fa')
count = 0
for key in readBack.keys():
    count += 1
    if readBack[key] in gene:
        success1 = 1
if count >= 9 and success1:
    print 'Passed Test9.2\n'
else:
    print 'Failed Test9.2\n'
    print count, success1
