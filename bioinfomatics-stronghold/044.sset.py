# https://rosalind.info/problems/sset/

# Counting Subsets

from math import comb


def load_data(filepath: str) -> int:
    with open(filepath, 'r') as f:
        n = int(f.readline().replace('\n', '').strip())
    return n


def subset_counts(n: int, module: int = 10 ** 6):
    count_sum = 0
    for i in range(0, n + 1):
        count_sum += comb(n, i)
    return count_sum % module


if __name__ == '__main__':
    inpath = "./datasets/044.sset.in"
    n = load_data(inpath)
    print(subset_counts(n))
