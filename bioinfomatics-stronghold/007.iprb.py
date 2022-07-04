# https://rosalind.info/problems/iprb/

import numpy as np

def load_kmn(filepath: str):
    k, m, n = 0, 0, 0
    with open(filepath, 'r') as f:
        k, m, n = [int(d) for d in f.readline().replace('\n', '').strip().split()]
    print(f'k: {k}, m: {m}, n: {n}')
    return k, m, n

def iprb(k: int, m: int, n: int):
    num_all = k + m + n
    # 后代为显性个体
    pr_list = []
    # AA x any
    pr_list.append(k / num_all)
    # Aa x AA
    pr_list.append(m / num_all * k / (num_all - 1))
    # Aa x Aa
    pr_list.append(m / num_all * (m - 1) / (num_all - 1) * 3 / 4)
    # Aa x aa
    pr_list.append(m / num_all * n / (num_all - 1) * 1 / 2)
    # aa x AA
    pr_list.append(n / num_all * k / (num_all - 1))
    # aa x Aa
    pr_list.append(n / num_all * m / (num_all - 1) * 1 / 2)
    # aa x aa
    pr_list.append(0)
    
    return np.sum(pr_list)
    
    
if __name__ == "__main__":
    path = './datasets/007.iprb.txt'
    k, m, n = load_kmn(path)
    print(iprb(k, m, n))