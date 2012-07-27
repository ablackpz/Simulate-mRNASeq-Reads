import sys, screed, os
import khmer

K = 32
N_HT=4

###

def main():
    htReads_filename = sys.argv[1]
    htExons_filename = sys.argv[2]
    contig_filename = sys.argv[3]

    print>>sys.stderr, 'loading ht from', htReads_filename
    htReads = khmer.new_counting_hash(K, 1, N_HT)
    htReads.load(htReads_filename)
    print >> sys.stderr, 'loading ht from', htExons_filename
    htExons = khmer.new_counting_hash(K, 1, N_HT)
    htExons.load(htExons_filename)
    htReadsAccounted = khmer.new_counting_hash(K, 1, N_HT)                    
    htRefAccounted = khmer.new_counting_hash(K, 1, N_HT)                       

#    countExons = htExons.n_entries()
#    countReads = htReads.n_entries()

    print >> sys.stderr, 'Beginning kmer count'

    cannotAssign = {}
    initialCount = 1
    for record in screed.open(contig_filename):
        cannotAssign[initialCount] = record.name
        initialCount += 1
    count = 0
    changes = 1

    while len(cannotAssign) != 0 and changes != 0:
        changes = 0
        for record in screed.open(contig_filename):
            if record.name not in cannotAssign:
                break
            seq = record.sequence.upper()
            if 'N' in seq:
                seq = seq.replace('N', 'G')
    
            medianCounts = []
            sum = 0
            for i in range (0, len(seq) - K):
                a = htReads.get(seq[i:i+K])
                b = htExons.get(seq[i:i+K])
                c = htReadsAccounted.get(seq[i:i+K])
                d = htRefAccounted.get(seq[i:i+K])
                if b == 1:
                    if a > -1:
                        medianCounts.append(a)
                elif b - d == 1:
                    if a - c > -1:
                        medianCounts.append(a - c)

            if len(medianCounts) > len(seq) / 10:
                medianCounts.sort()
                for i in range(0, len(medianCounts)):
                    sum += medianCounts[i]
                average = sum / len(medianCounts)
                if len(medianCounts) % 2:
                    median = medianCounts[len(medianCounts) // 2]
                else:
                    median = float(medianCounts[len(medianCounts) / 2 - 1] + medianCounts[len(medianCounts) / 2]) / 2
                print '%s %6.0f %6.0f %1.0f' % (record.name, median, average, len(seq))
                htRefAccounted.consume(seq)
                for z in range(0, int(median)):
                    htReadsAccounted.consume(seq)
                changes = 1

            else:
                median = -1
                average = -1
                cannotAssign[count] = record.name
                count += 1
#                print '%s %6.0f %6.0f %1.0f' % (record.name, median, average, len(seq))

    for i in range(0, count):
#        print >> sys.stderr, cannotAssign[i]
        print '%s %6.0f %6.0f %1.0f' % (cannotAssign[i], -1, -1, 0))

#    htReadsAccounted = khmer.new_counting_hash(K, 1, N_HT)
#    htRefAccounted = khmer.new_counting_hash(K, 1, N_HT)
    print >> sys.stderr, 'Finished!'

if __name__ == '__main__':
    main()
