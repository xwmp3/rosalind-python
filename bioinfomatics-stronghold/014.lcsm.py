# https://rosalind.info/problems/lcsm/

import numpy as np

def timer(func):
    def func_wrapper(*args,**kwargs):
        from time import time
        time_start = time()
        result = func(*args,**kwargs)
        time_end = time()
        print('{0} cost time {1} s'.format(func.__name__, time_end - time_start))
        return result
    return func_wrapper

def load_fasta(filepath: str):
    name_list, seq_list = [], []
    with open(filepath, 'r') as fasta:
        while True:
            line = fasta.readline()
            if not line:
                break
            data = line.replace('\n', '').strip()
            if data.startswith('>'):
                name_list.append(data[1:])
                line = fasta.readline().replace('\n', '').strip()
                seq_list.append(line)
            else:
                seq_list[len(seq_list) - 1] += line.replace('\n', '').strip()
    return name_list, seq_list

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