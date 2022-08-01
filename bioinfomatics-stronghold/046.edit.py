# https://rosalind.info/problems/edit/

# Edit Distance

from data import load_fasta
import numpy as np

def load_data(filepath: str) -> int:
    with open(filepath, 'r') as f:
        s1, s2 = load_fasta(filepath)[1]
    return s1, s2

def edit_distance(s1: str, s2: str) -> int:
    i = j = 0
    m, n = len(s1), len(s2)
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
            if s1[x - 1] == s2[y - 1]:
                flag = 0
            else:
                flag = 1
            d[x][y] = min(
                d[x][y-1] + 1,
                d[x-1][y] + 1,
                d[x-1][y-1] + flag
            )
    return d[m][n]

if __name__ == '__main__':
    inpath = "./datasets/046.edit.txt"
    s1, s2 = load_data(inpath)
    print(edit_distance(s1, s2))
