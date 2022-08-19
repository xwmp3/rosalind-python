# https://rosalind.info/problems/pper/

from itertools import permutations
from math import factorial


def load_data(filepath: str) -> tuple:
    n, k = 0, 0
    with open(filepath, 'r') as f:
        n, k = [int(d) for d in f.readline().replace('\n', '').strip().split()]
    return n, k


def partial_permutation_with_modulo(n: int, k: int, modulo: int = 1000000):
    # return sum(1 for _ in permutations(range(n), k)) % modulo
    return int(factorial(n) / factorial(n - k) % modulo)


if __name__ == '__main__':
    path = "./datasets/027.pper.txt"
    n, k = load_data(path)
    print(n, k)
    print(partial_permutation_with_modulo(n, k))
