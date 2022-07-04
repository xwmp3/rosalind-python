# https://rosalind.info/problems/fibd/

import numpy as np

def fibd_none_recursive(n: int, m: int):
    fib_table = []
    for i in range(n):
        if i < 2:
            fib_table.append(1)
        elif i < m:
            fib_table.append(fib_table[-2] + fib_table[-1])
        elif i == m or i == m + 1:
            fib_table.append(fib_table[-2] + fib_table[-1] - fib_table[-m])
        else:
            fib_table.append(fib_table[-2] + fib_table[-1] - fib_table[-(m + 1)])
    return fib_table[n - 1]

    
if __name__ == '__main__':
    path = './datasets/011.fibd.txt'
    n, m = 0, 0
    with open(path, 'r') as f:
        n, m = [int(d) for d in f.readline().replace('\n', '').strip().split()]
    print(f"n: {n}, m: {m}")
    print(fibd_none_recursive(n, m))