# https://rosalind.info/problems/fibd/

from typing import Tuple


def load_data(filepath: str) -> Tuple[int, int]:
    with open(path, 'r') as f:
        n, m = [int(d) for d in f.readline().replace('\n', '').strip().split()]
    return n, m


def fibd_recursive(n: int, m: int):
    if n == 1 or n == 2:
        return 1
    elif n <= m:
        return fibd_recursive(n - 1, m) + fibd_recursive(n - 2, m)
    elif n == m + 1:
        return fibd_recursive(n - 1, m) + fibd_recursive(n - 2, m) - fibd_recursive(n - m, m)
    else:
        return fibd_recursive(n - 1, m) + fibd_recursive(n - 2, m) - fibd_recursive(n - m - 1, m)


def fibd_non_recursive(n: int, m: int):
    fib_table = []
    for i in range(n):
        if i < 2:
            fib_table.append(1)
        elif i < m:
            fib_table.append(fib_table[-2] + fib_table[-1])
        elif i == m:
            fib_table.append(fib_table[-2] + fib_table[-1] - fib_table[-m])
        else:
            fib_table.append(fib_table[-2] + fib_table[-1] - fib_table[-(m + 1)])
    return fib_table[n - 1]


if __name__ == '__main__':
    path = 'datasets/011.fibd.in'
    n, m = load_data(path)
    print(f"n: {n}, m: {m}")
    # print(f"recursive: \t{fibd_recursive(n, m)}")
    print(f"non-recursive: \t{fibd_non_recursive(n, m)}")
