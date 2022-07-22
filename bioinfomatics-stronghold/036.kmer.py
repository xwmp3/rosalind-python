# https://rosalind.info/problems/kmer/

from itertools import product

def load_fasta(filepath: str):
    name_list, seq_list = [], []
    with open(filepath, 'r') as fasta:
        while True:
            line = fasta.readline()
            if not line:
                break
            data = line.replace('\n', '').strip()
            if data.startswith('>'):
                name_list.append(data[1:])
                line = fasta.readline().replace('\n', '').strip()
                seq_list.append(line)
            else:
                seq_list[len(seq_list) - 1] += line.replace('\n', '').strip()
    return name_list, seq_list

def load_data(filepath: str):
    return load_fasta(filepath)[1][0]

def generate_dna_kmers(k: int=4):
    dna_n_list = ['A', 'C', 'G', 'T']
    kmers = []
    for kmer in product(dna_n_list, repeat=k):
        kmers.append(''.join(kmer))
    return kmers

def find_all(s: str, t: str) -> int:
    count = 0
    for i in range(0, len(s) - len(t) + 1):
        if s[i : i + len(t)] == t:
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

