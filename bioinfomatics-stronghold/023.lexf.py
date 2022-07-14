# https://rosalind.info/problems/lexf/

from itertools import product

def load_data(filepath: str):
    symbols, n = [], 0
    with open(filepath, 'r') as f:
        symbols = f.readline().replace('\n', '').strip().split()
        n = int(f.readline().replace('\n', '').strip())
    return symbols, n

def enumerate_kmers(symbols: list, n: int) -> list:
    res = []
    for data in product(symbols, repeat=n):
        res.append(''.join(data))
    return res

if __name__ == '__main__':
    path = "./datasets/023.lexf.txt"
    symbols, n = load_data(path)
    print(symbols, n)
    for d in enumerate_kmers(symbols, n):
        print(d)