# https://rosalind.info/problems/prob/

from math import log10

from utils import motif_prob


def load_data(filepath: str) -> (str, list):
    with open(filepath, 'r') as f:
        s = f.readline().replace('\n', '').strip()
        gc_contents = [float(item) for item in f.readline().replace('\n', '').strip().split()]
    return s, gc_contents


if __name__ == '__main__':
    path = "./datasets/028.prob.txt"
    s, gc_cs = load_data(path)
    print(' '.join([str(round(log10(motif_prob(s, gc_content)), 3)) for gc_content in gc_cs]))
