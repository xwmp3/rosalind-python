# https://rosalind.info/problems/prob/

from math import log10

def load_data(filepath: str) -> (str, list):
    s, gc_contents = "", []
    with open(filepath, 'r') as f:
        s = f.readline().replace('\n', '').strip()
        gc_contents = [float(item) for item in f.readline().replace('\n', '').strip().split()]
    return s, gc_contents

def random_string_prob(s: str, gc_content: float):
    gc_prob, at_prob = gc_content / 2, (1 - gc_content) / 2
    prob = 1
    for n in s:
        if n == 'A' or n == 'T':
            prob *= at_prob
        elif n == 'C' or n == 'G':
            prob *= gc_prob
    return prob
    
if __name__ == '__main__':
    path = "./datasets/028.prob.txt"
    s, gc_cs = load_data(path)
    print(' '.join([str(round(log10(random_string_prob(s, gc_content)), 3)) for gc_content in gc_cs]))