# https://rosalind.info/problems/revp/

from data import load_fasta
from utils import dna_reverse_implement


def palindromic_recognition_site(seq1: str):
    res: list = []
    seq2 = dna_reverse_implement(seq1)[::-1]
    for i in range(2, len(seq2) - 1):
        for j in range(2, 7):
            if i - j < 0 or i + j > len(seq2): break
            if seq1[i - j:i] == seq2[i:i + j][::-1] and seq2[i - j:i] == seq1[i:i + j][::-1]:
                res.append((i - j + 1, i + j - (i - j)))
    return res


if __name__ == '__main__':
    inpath = "./datasets/021.revp.txt"
    outpath = "./datasets/021.revp.out"
    seq = load_fasta(inpath)[1][0]
    with open(outpath, 'w') as f:
        for pos, length in palindromic_recognition_site(seq):
            f.write(f"{pos} {length}\n")
    print(f"Save Results to {outpath}")
