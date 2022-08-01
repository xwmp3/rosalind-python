def timer(func):
    def func_wrapper(*args,**kwargs):
        from time import time
        time_start = time()
        result = func(*args,**kwargs)
        time_end = time()
        print('{0} cost time {1} s'.format(func.__name__, time_end - time_start))
        return result
    return func_wrapper

def hamming_distance(s1: str, s2: str):
    if len(s1) != len(s2):
        raise ValueError("Not the same length!")
    return sum(es1 != es2 for es1, es2 in zip(s1, s2))

def count_nucleotides(seq: str, nmap: str="ACGT") -> list:
    counts = [0 for _ in range(len(nmap))]
    for n in seq:
        counts[nmap.index(n)] += 1
    return counts

def dna_2_rna(seq: str) -> str:
    return ''.join([n if n != 'T' else 'U' for n in seq])

def dna_reverse_implement(seq: str) -> str:
    reverse_seq = seq[::-1]
    res = []
    for n in reverse_seq:
        if n == 'A':
            res.append('T')
        elif n == 'T':
            res.append('A')
        elif n == 'C':
            res.append('G')
        elif n == 'G':
            res.append('C')
    return ''.join(res)

def motif_prob(s: str, gc_content: float):
    gc_prob, at_prob = gc_content / 2, (1 - gc_content) / 2
    prob = 1
    for n in s:
        if n == 'A' or n == 'T':
            prob *= at_prob
        elif n == 'C' or n == 'G':
            prob *= gc_prob
    return prob
