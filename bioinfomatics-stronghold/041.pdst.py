# https://rosalind.info/problems/pdst/

# Creating a Distance Matrix

from data import load_fasta
from utils import hamming_distance
import numpy as np


def load_data(filepath: str) -> (int, list):
    seqs = load_fasta(filepath)[1]
    return len(seqs[0]), seqs


def p_distance(s1: str, s2: str):
    h_d = hamming_distance(s1, s2)
    return h_d / len(s1)


def distance_matrix(n_length: int, seqs: list):
    dist_mat = np.zeros((len(seqs), len(seqs)))
    for i in range(len(seqs)):
        for j in range(i + 1, len(seqs)):
            dist_mat[i][j] = dist_mat[j][i] = p_distance(seqs[i], seqs[j])
    return dist_mat


def save_d_matrix(filepath: str, d_mat: np.ndarray, n_round: int):
    with open(filepath, 'w') as f:
        f.write('\n'.join([' '.join([format(d, f'.{n_round}f') for d in row]) for row in d_mat]))


if __name__ == '__main__':
    inpath = "./datasets/041.pdst.txt"
    outpath = "./datasets/041.pdst.out"
    seq_length, seqs = load_data(inpath)
    print(f"seq length: {seq_length}\nfasta seq: {seqs}")
    d_m = distance_matrix(seq_length, seqs)
    save_d_matrix(outpath, d_m, 5)
    print(f"Save Results to {outpath}")
