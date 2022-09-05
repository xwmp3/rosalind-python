# https://rosalind.info/problems/splc/

from data import load_fasta, load_rna_codon_table
from utils import dna_2_rna


def load_data(filepath: str):
    seqs = load_fasta(filepath)[1]
    dna_seq, intron_seqs = seqs[0], seqs[1:]
    return dna_seq, intron_seqs


def get_exon_concatenated(dna: str, introns: list) -> str:
    for intron in introns:
        dna = dna.replace(intron, '')
    return dna


def rna2prot(rna_prot_map: dict, seq: str):
    prot_list = []
    for i in range(int(len(seq) / 3)):
        prot = rna_prot_map[seq[3 * i: 3 * i + 3]]
        if prot == 'Stop':
            break
        prot_list.append(prot)
    return ''.join(prot_list)


if __name__ == '__main__':
    path = "datasets/022.splc.in"
    codon_map = load_rna_codon_table()
    dna, introns = load_data(path)
    exon_concat = get_exon_concatenated(dna, introns)
    rna = dna_2_rna(exon_concat)
    prot = rna2prot(codon_map, rna)
    print(prot)
