# https://rosalind.info/problems/mmch/

# Maximum Matchings and RNA Secondary Structures

from utils import count_nucleotides, load_fasta

def load_data(filepath: str) -> str:
    return load_fasta(filepath)[1][0]

from math import factorial

def nPr(n, r):
    return factorial(n) // factorial(n - r)

def maximum_matching_num(seq: str) -> int:
    a_count, c_count, g_count, u_count = count_nucleotides(seq=[n for n in seq], nmap='ACGU')
    au_counts, cg_counts = [a_count, u_count], [c_count, g_count]
    return nPr(max(au_counts), min(au_counts)) * nPr(max(cg_counts), min(cg_counts))

if __name__ == '__main__':
    inpath = "./datasets/040.mmch.txt"
    outpath = "./datasets/040.mmch.out"
    seq = load_data(inpath)
    print(f"fasta seq: {seq}")
    with open(outpath, 'w') as f:
        f.write(f"{mmch(seq)}\n")
    print(f"Save Results to {outpath}")

