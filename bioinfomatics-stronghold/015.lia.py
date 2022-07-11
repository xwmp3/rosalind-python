# https://rosalind.info/problems/lia/

from scipy.special import comb
from scipy.stats import binom

def load_data(filepath: str) -> tuple:
    k, N = 0, 0
    with open(filepath, 'r') as f:
        k, N = [int(d) for d in f.readline().replace('\n', '').strip().split()]
    return k, N

# solution 1
def ida(k: int, N: int):
    prob = 0
    for i in range(N, 2 ** k + 1):
        prob += comb(2**k, i) * ((1/4.0)**i) * ((3/4.0)**((2**k)-i))
    return prob

# solution 2: using the cdf from `scipy` package
def ida_binom(k: int, N: int):
    return binom.cdf(2**k - N, 2**k, 0.75)
        
if __name__ == '__main__':
    path = './datasets/015.lia.txt'
    k, N = load_data(path)
    print(f"k: {k}, N: {N}.\nProb of 'AaBb': {ida_binom(k, N)}")