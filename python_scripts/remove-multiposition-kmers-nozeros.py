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

#    countExons = htExons.n_entries()
#    countReads = htReads.n_entries()
#    print countExons
#    print countReads

    print >> sys.stderr, 'Beginning kmer count'

    for record in screed.open(contig_filename):
        seq = record.sequence.upper()
        if 'N' in seq:
            seq = seq.replace('N', 'G')
    
        medianCounts = []
        sum = 0
        for i in range (0, len(seq) - K):
            a, b, c = htReads.get_median_count(seq[i:i+K])
            d, e, f = htExons.get_median_count(seq[i:i+K])
            if d < 2:
                if a > 0:
                    medianCounts.append(a)
#            medianCounts.append(a / d) if a and d else medianCounts.append(a)

        
        if len(medianCounts) > len(seq) / 10:
            medianCounts.sort()
            for i in range(0, len(medianCounts)):
                sum += medianCounts[i]
            average = sum / len(medianCounts)
            if len(medianCounts) % 2:
                median = medianCounts[len(medianCounts) // 2]
            else:
                median = float(medianCounts[len(medianCounts) / 2 - 1] + medianCounts[len(medianCounts) / 2]) / 2
        else:
            median = -1
            average = -1

        print '%s %6.0f %6.0f %1.0f' % (record.name, median, average, len(seq))


print >> sys.stderr, 'Finished!'

if __name__ == '__main__':
    main()
