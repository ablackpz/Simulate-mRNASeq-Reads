# A script to make a R command file that will make graphs for median, simulated, and bowtie data
# Created: 2011.10.20
# Original Author: A. Black P.
# Last Modified: 2011.11.03
# Last Author: A. Black P.

fileHandle = 'DataSet'
outfileName = 'DataSet.R'
loopBegin = 89
loopEnd = 89

s12 = r'bt <- scan("'
s13 = r'_default.map.geneExpNum")'
s14 = r'pdf("'
s15 = r'_defaultBowtie.pdf")'
s16 = r'barplot(bt, col=9, font=2)'
s17 = r'dev.off()'


outfile = open(outfileName, 'w')
for i in range(loopBegin, loopEnd + 1):
    outfile.write(s12 + fileHandle + str(i) + s13 + '\n')
    outfile.write(s14 + fileHandle + str(i) + s15 + '\n')
    outfile.write(s16 + '\n')
    outfile.write(s17 + '\n')

outfile.close()
print 'Finished'
