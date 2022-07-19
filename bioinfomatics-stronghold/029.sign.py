# https://rosalind.info/problems/sign/

from itertools import permutations, product
import numpy as np

def load_data(filepath: str) -> int:
    n = 0
    with open(filepath, 'r') as f:
        n = int(f.readline().replace('\n', '').strip())
    return n

def concat(nums: list, signs: list) -> list:
    return [str(nums[i]) if str(signs[i]) == '1' else '-'+str(nums[i]) for i in range(len(nums))]

def signed_permute(n: int) -> list:
    res_list = []
    src_list = [d for d in permutations([i for i in range(1, n + 1)])]
    sign_list = [[k for k in format(d, f"0{n}b")] for d in [i for i in range(0, n*n)]]
    for src, sign in product(src_list, sign_list):
        res_list.append(concat(src, sign))
    return res_list
    
if __name__ == '__main__':
    path = "./datasets/029.sign.txt"
    n = load_data(path)
    permutes = signed_permute(n)
    print(len(permutes))
    for res in permutes:
        print(' '.join([str(item) for item in res]))