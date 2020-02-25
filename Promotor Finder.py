#script needs a qualifying section which selects promotors only occuring in intergenic regions with a downstream atg i.e. correct orientated CDS#

from Bio import SeqIO
from Bio.Seq import Seq

forseq = "TTTACA" # Just use python strings here. No Seq() as above
revseq = "NTNNTN"
filename = "/Users/ryanjhope/Documents/PhD/DNA_Sequences/Genome/Campylobacter_jejuni/NC_002163.1.fasta"

revcomp = {'A':'T', 'C':'G', 'G':'C', 'T':'A',
           'R':'Y', 'Y':'R', 'S':'S', 'W':'W',
           'K':'M', 'M':'K', 'B':'V', 'V':'B',
           'D':'H', 'H':'D', 'N':'N'}
redund = {'A':['A'], 'C':['C'], 'G':['G'], 'T':['T'],
          'R':['A','G'], 'Y':['C','T'],
          'S':['C','G'], 'W':['A','T'],
          'K':['G','T'], 'M':['A','C'],
          'B':['C','G','T'], 'V':['A','C','G'],
          'D':['A','G','T'], 'H':['A','C','T'],
          'N':['A','C','G','T']}

def revcom(seq):
    return "".join(revcomp.get(base, base) for base in reversed(seq))

def seqmatch(query, reference):
    """Checks if the query sequence (perhaps a promoter with redundant bases)
    matches the reference. Both query and reference must be the same length.

    Returns true if there is a match (redundancy allowed), returns false
    otherwise.
    """
    assert len(query) == len(reference)
    for i in range(len(query)):
        if reference[i] in redund[query[i]]:
            pass
        else:
            return False
    return True

forseq = forseq.upper()
revseq = revseq.upper()
forcom = revcom(forseq)
revcom = revcom(revseq)
print("seq\tstart\tstop\tgap\tdir\tseq")
for record in SeqIO.parse(filename, "fasta"):
    for i in range(len(record.seq)):
        for v1, v2, direc in [ (forseq, revseq, "F"), (revcom, forcom, "R") ]:
            if seqmatch( v1, record.seq[i:i+len(v1)] ):
                for j in range(17,18):
                    if seqmatch( v2, record.seq[i+len(v1)+j:i+len(v2)+j+len(v2)] ):
                        print("{}\t{}\t{}\t{}\t{}\t{}".format(
                            record.id, i,
                            i + len(v1)+j+len(v2)-1,
                            j, direc,
                            record.seq[i: i+len(v1) + j + len(v2)] ))
