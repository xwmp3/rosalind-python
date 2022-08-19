# https://rosalind.info/problems/aspc/

# Introduction to Alternative Splicing

from math import comb


def load_data(filepath: str) -> int:
    with open(filepath, 'r') as f:
        n, m = [int(item) for item in f.readline().replace('\n', '').strip().split()]
    return n, m


def alternative_splicing_counts(n: int, m: int, module: int = 10 ** 6) -> int:
    """

    @param n:
    @param m:
    @param module:
    @return:
    """
    count_sum = 0
    for i in range(m, n + 1):
        count_sum += comb(n, i)

    return count_sum % module


if __name__ == '__main__':
    inpath = "./datasets/045.aspc.txt"
    n, m = load_data(inpath)
    print(alternative_splicing_counts(n, m))
