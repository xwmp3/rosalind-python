# https://rosalind.info/problems/kmer/

from itertools import product

from data import load_fasta


def load_data(filepath: str):
    return load_fasta(filepath)[1][0]


def generate_dna_kmers(k: int = 4):
    dna_n_list = ['A', 'C', 'G', 'T']
    kmers = []
    for kmer in product(dna_n_list, repeat=k):
        kmers.append(''.join(kmer))
    return kmers


def find_all(s: str, t: str) -> int:
    count = 0
    for i in range(0, len(s) - len(t) + 1):
        if s[i: i + len(t)] == t:
            count += 1
    return count


def kmers_composition(seq: str, kmers: list):
    return [find_all(seq, kmer) for kmer in kmers]


if __name__ == '__main__':
    path = "./datasets/036.kmer.txt"
    outpath = './datasets/036.kmer.out'
    seq = load_data(path)
    kmers = generate_dna_kmers()
    with open(outpath, 'w') as f:
        f.write(' '.join([str(count) for count in kmers_composition(seq, kmers)]) + '\n')
    print(f"Save K-Mer Composition to {outpath}.")
