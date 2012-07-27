# A script to take a set of transcripts and produce overlapping reads for all transcripts for use in finding transcript families

# Usage: python testTranscripts.py input.fa output.fa readLength

import sys, makeRandomTestData

inputFileName = sys.argv[1]
outputFileName = sys.argv[2]
readLength = int(sys.argv[3])

transcripts = makeRandomTestData.inputFastaSeq(inputFileName)

for i in sorted(transcripts):
    complete = makeRandomTestData.makeAllOverlapReads(readLength, transcripts[i], i, outputFileName)

print 'Finished!'
