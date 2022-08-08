# https://rosalind.info/problems/eval/

# Expected Number of Restriction Sites

'''
finding an expected number of events to finding the expected number of times 
    that a given string occurs as a substring of a random string.
'''

from scipy.stats import binom
from utils import motif_prob

def load_data(filepath: str):
    with open(filepath, 'r') as f:
        n = int(f.readline().replace('n', '').strip())
        s = f.readline().replace('n', '').strip()
        gc_contents = [float(item) for item in f.readline().replace('n', '').strip().split()]
    
    return n, s, gc_contents

def expected_number(n: int, s: str, gc_content: float):
    prob = motif_prob(s, gc_content)
    return prob * (n - len(s) + 1)

if __name__ == "__main__":
    inpath = "./datasets/047.eval.txt"
   
    n, s, gc_contents = load_data(inpath)
    print(n, s, gc_contents)
    
    res = [round(expected_number(n, s, gc), 3) for gc in gc_contents]
    print(' '.join([str(item) for item in res]))
