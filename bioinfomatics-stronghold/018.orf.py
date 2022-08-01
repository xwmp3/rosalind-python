# https://rosalind.info/problems/orf/

from data import load_fasta, load_rna_codon_table
from utils import dna_reverse_implement, dna_2_rna 

def rna_2_prot(seq: str, codon_map: dict, start_codon: str='AUG') -> list:
    prot_set = set()
    for i in range(0, len(seq) - 3):
        if seq[i:i+3] == start_codon:
            orf_seq = seq[i:]
            animo_list = [codon_map[orf_seq[3*j: 3*j+3]] for j in range(int(len(orf_seq) / 3))]
            if 'Stop' in animo_list:
                prot_set.add(''.join(animo_list[:animo_list.index('Stop')]))
    return prot_set

if __name__ == '__main__':
    path = './datasets/018.orf.txt'
    data = load_fasta(path)[1][0]
    rna_codon_map = load_rna_codon_table()
    seqs = [data, dna_reverse_implement(data)]
    prots = set()
    for seq in seqs:
        rna_seq = dna_2_rna(seq)
        print(rna_seq)
        for p in rna_2_prot(rna_seq, rna_codon_map):
            prots.add(p)
    print("\n".join(list(prots)))