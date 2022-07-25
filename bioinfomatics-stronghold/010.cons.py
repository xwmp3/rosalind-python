# https://rosalind.info/problems/cons/

import numpy as np

from utils import load_fasta

def count_nucleotides(seq: str, nmap: str="ACGT"):
    counts = [0 for _ in range(len(nmap))]
    for n in seq:
        counts[nmap.index(n)] += 1
    return counts

def profile_and_consensus(names: list, seqs: list, nmap: str='ACGT'):
    cols = []
    count_list = [[] for _ in range(len(nmap))]
    index_list = []
    for i in range(0, len(seqs[0])):
        col = []
        for j in range(0, len(names)):
            col.append(seqs[j][i])
        cols.append(col)
        counts = count_nucleotides(col, nmap)
        for i in range(len(nmap)):
            count_list[i].append(counts[i])
        index_list.append(np.argmax(counts))
    return index_list, count_list


if __name__ == '__main__':
    path = './datasets/010.cons.txt'
    nmap = 'ACGT'
    names, seqs = load_fasta(path)
    index_list, count_list = profile_and_consensus(names, seqs, nmap)
    print(''.join([nmap[i] for i in index_list]))
    for i, n in enumerate(nmap):
        print(f"{n}: {' '.join([str(count) for count in count_list[i]])}")