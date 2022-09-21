# https://rosalind.info/problems/splc/

from data import load_fasta
from utils import dna_2_rna, rna_2_protein, list_2_str


def load_data(filepath: str):
    seqs = load_fasta(filepath)[1]
    dna_seq, intron_seqs = seqs[0], seqs[1:]
    return dna_seq, intron_seqs


def get_exon_concatenated(dna: str, introns: list) -> str:
    for intron in introns:
        dna = dna.replace(intron, '')
    return dna


if __name__ == '__main__':
    path = "datasets/022.splc.in"

    dna, introns = load_data(path)
    exon_concat = get_exon_concatenated(dna, introns)
    rna = dna_2_rna(exon_concat)
    prot = rna_2_protein(rna)

    print(list_2_str(prot, sep=''))
