# https://rosalind.info/problems/pmch/

from math import factorial

from data import load_fasta

def load_data(filepath: str) -> str:
    return load_fasta(path)[1][0]

def perfect_match_num(seq: str) -> int:
    au_count, cg_count = 0, 0
    for n in seq:
        if n == 'A' or n == 'U':
            au_count += 1
        elif n == 'C' or n == 'G':
            cg_count += 1
    return factorial(int(au_count / 2)) * factorial(int(cg_count / 2))
    
if __name__ == '__main__':
    path = "./datasets/026.pmch.txt"
    rna_seq = load_data(path)
    print(rna_seq)
    print(perfect_match_num(rna_seq))