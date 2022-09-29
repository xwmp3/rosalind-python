# https://rosalind.info/problems/perm/

import itertools

from utils import list_2_str


def load_n(filepath: str) -> int:
    with open(filepath, 'r') as f:
        n = int(f.readline().replace('\n', '').strip())
    return n


# https://docs.python.org/zh-cn/3/library/itertools.html#itertools.permutations
def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n - r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i + 1:] + indices[i:i + 1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return


def get_permutation_list(n: int):
    n_list = [i for i in range(1, n + 1)]
    res = []
    for permutation in permutations(n_list):
        res.append(permutation)
    return res


if __name__ == '__main__':
    inpath = "datasets/019.perm.in"

    permutate_list = get_permutation_list(load_n(inpath))
    print(len(permutate_list))
    for perm in permutate_list:
        print(list_2_str(perm))
