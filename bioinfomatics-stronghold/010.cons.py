# https://rosalind.info/problems/cons/

import numpy as np

from data import load_fasta
from utils import count_nucleotides


def profile_and_consensus(names: list, seqs: list, nmap: str = 'ACGT'):
    cols = []
    count_list = [[] for _ in range(len(nmap))]
    index_list = []
    for i in range(0, len(seqs[0])):
        col = ""
        for j in range(0, len(names)):
            col += seqs[j][i]
        cols.append(col)
        counts = count_nucleotides(col, nmap)
        for i in range(len(nmap)):
            count_list[i].append(counts[i])
        index_list.append(np.argmax(counts))
    return index_list, count_list


if __name__ == '__main__':
    inpath = './datasets/010.cons.txt'
    outpath = './datasets/010.cons.out'
    nmap = 'ACGT'
    names, seqs = load_fasta(inpath)
    index_list, count_list = profile_and_consensus(names, seqs, nmap)
    outstr = ""
    for i, n in enumerate(nmap):
        outstr += f"{n}: {' '.join([str(count) for count in count_list[i]])}\n"
    print(outstr)
    with open(outpath, 'w') as f:
        f.write(outstr)
    print(f"Save Results to {outpath}")
