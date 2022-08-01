# https://rosalind.info/problems/lcsm/

import numpy as np

from data import load_fasta
from utils import timer

def get_subs(s: str, sort: bool=True):
    subs = []
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            subs.append(s[i:j])
    if sort:
        subs = sorted(subs, key=lambda i : len(i), reverse=True)
    return subs

def is_substr(s: str, t: str):
    for i in range(0, len(s) - len(t)):
        if s[i: i + len(t)] == t:
            return True
    return False

@timer
def longest_common_substring1(seqs: list):
    shortest_seq = min(seqs, key=len)
    sub_seqs = get_subs(shortest_seq)
    for t in sub_seqs:
        ks = []
        for s in seqs:
            if not is_substr(s, t):
                break
            else:
                ks.append(1)
        if np.sum(ks) == len(seqs):
            return t
    return None

# https://stackoverflow.com/a/32611507
@timer
def longest_common_substring2(data: list):
    substrs = lambda x: {x[i:i+j] for i in range(len(x)) for j in range(len(x) - i + 1)}
    s = substrs(data[0])
    for val in data[1:]:
        s.intersection_update(substrs(val))
    return max(s, key=len)
    
if __name__ == '__main__':
    path = './datasets/014.lcsm.txt'
    names, seqs = load_fasta(path)
    lcs = longest_common_substring1(seqs)
    print(lcs)
    lcs = longest_common_substring2(seqs)
    print(lcs)