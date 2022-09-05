# https://rosalind.info/problems/perm/

from itertools import permutations


def load_n(filepath: str) -> int:
    n: int = 0
    with open(filepath, 'r') as f:
        n = int(f.readline().replace('\n', '').strip())
    return n


def get_permutation_list(n: int):
    n_list = [i for i in range(1, n + 1)]
    print(n_list)
    return [iter_list for iter_list in permutations(n_list)]


if __name__ == '__main__':
    path = "datasets/019.perm.in"
    n = load_n(path)
    print(n)
    permutate_list = get_permutation_list(n)
    print(len(permutate_list))
    for iter_list in permutate_list:
        print(' '.join([str(item) for item in iter_list]))
