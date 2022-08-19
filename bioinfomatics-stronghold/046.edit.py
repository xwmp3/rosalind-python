# https://rosalind.info/problems/edit/

# Edit Distance

from typing import Tuple
from data import load_fasta


def load_data(filepath: str) -> Tuple[str, str]:
    return load_fasta(filepath)[1]


def edit_distance(seq1: str, seq2: str) -> int:
    i = j = 0
    m, n = len(seq1), len(seq2)
    if m == 0:
        return n
    if n == 0:
        return m
    d = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m + 1):
        d[i][0] = i
    for j in range(n + 1):
        d[0][j] = j
    for x in range(1, m + 1):
        for y in range(1, n + 1):
            if seq1[x - 1] == seq2[y - 1]:
                flag = 0
            else:
                flag = 1
            d[x][y] = min(
                d[x][y - 1] + 1,
                d[x - 1][y] + 1,
                d[x - 1][y - 1] + flag
            )
    return d[m][n]


if __name__ == '__main__':
    inpath = "./datasets/046.edit.txt"
    s1, s2 = load_data(inpath)
    print(edit_distance(s1, s2))
