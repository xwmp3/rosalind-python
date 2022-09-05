# https://rosalind.info/problems/lexv/

# Ordering Strings of Varying Length Lexicographically

from itertools import product


def load_data(filepath: str) -> (list, int):
    with open(filepath, 'r') as f:
        symbols = f.readline().replace('\n', '').strip().split()
        n = int(f.readline().replace('\n', '').strip())
    return symbols, n


def lexv(symbols: list, n: int):
    res = []
    for temp in product(symbols, repeat=n):
        for i in range(1, n + 1):
            if temp[:i] not in res:
                res.append(temp[:i])
    return res


if __name__ == '__main__':
    inpath = "./datasets/039.lexv.in"
    outpath = "./datasets/039.lexv.out"
    s, n = load_data(inpath)
    print(s, n)
    res = lexv(s, n)
    with open(outpath, 'w') as f:
        for item in res:
            f.write(f"{''.join(item)}\n")
    print(f"Save Results to {outpath}")
