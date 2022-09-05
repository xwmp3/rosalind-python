# https://rosalind.info/problems/lgis/

import numpy as np
from math import floor


def load_data(filepath: str):
    with open(filepath, 'r') as f:
        n = int(f.readline().replace('\n', '').strip())
        X = [int(item) for item in f.readline().replace('\n', '').strip().split()]
    return n, X


# https://en.wikipedia.org/wiki/Longest_increasing_subsequence
def longest_increasing_subseq(N: int, X: list) -> np.ndarray:
    P, M = np.zeros(n, dtype=int), np.zeros(n + 1, dtype=int)
    M[0] = -1
    L = 0
    for i in range(0, N):
        # 二分查找最小元素位置
        low, high = 1, L + 1
        while low < high:
            mid = low + floor((high - low) / 2)
            if X[M[mid]] > X[i]:
                high = mid
            else:
                low = mid + 1
        newL = low
        P[i] = M[newL - 1]
        M[newL] = i
        if newL > L:
            L = newL
    S = np.zeros(L, dtype=int)
    k = M[L]
    for j in range(L - 1, -1, -1):
        S[j] = X[k]
        k = P[k]
    return S


if __name__ == '__main__':
    path = "datasets/024.lgis.in"
    n, X = load_data(path)
    print(' '.join([str(item) for item in longest_increasing_subseq(n, X)]))
    print(' '.join([str(item) for item in longest_increasing_subseq(n, X[::-1])[::-1]]))
