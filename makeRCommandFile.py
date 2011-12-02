# A script to make a R command file that will make graphs for median, simulated, and bowtie data
# Created: 2011.10.20
# Original Author: A. Black P.
# Last Modified: 2011.10.20
# Last Author: A. Black P.

fileHandle = 'DataSet'
outfileName = 'DataSet.R'
loopBegin = 130
loopEnd = 130

s1 = r'med <- scan("'
s2 = r'.outMed")'
s3 = r'pdf("'
s4 = r'Actual.pdf")'
s5 = r'barplot(med, col=4, font=2)'
s6 = r'dev.off()'
s7 = r'ex <- scan("'
s18 = r'.txtActual")'
s8 = r'pdf("'
s9 = r'Theoretical.pdf")'
s10 = r'barplot(ex, col=2, font=2)'
s11 = s6
s12 = r'bt <- scan("'
s13 = r'.map.geneExpNum")'
s14 = r'pdf("'
s15 = r'Bowtie.pdf")'
s16 = r'barplot(bt, col=9, font=2)'
s17 = s6


outfile = open(outfileName, 'w')
for i in range(loopBegin, loopEnd + 1):
    outfile.write(s1 + fileHandle + str(i) + s2 + '\n')
    outfile.write(s3 + fileHandle + str(i) + s4 + '\n')
    outfile.write(s5 + '\n')
    outfile.write(s6 + '\n')
    outfile.write(s7 + fileHandle + str(i) + s18 + '\n')
    outfile.write(s8 + fileHandle + str(i) + s9 + '\n')
    outfile.write(s10 + '\n')
    outfile.write(s11 + '\n')
    outfile.write(s12 + fileHandle + str(i) + s13 + '\n')
    outfile.write(s14 + fileHandle + str(i) + s15 + '\n')
    outfile.write(s16 + '\n')
    outfile.write(s17 + '\n')

outfile.close()
print 'Finished'
