# https://rosalind.info/problems/rstr/

# Matching Random Motifs 

from scipy.stats import binom

from utils import motif_prob

def load_data(filepath: str) -> (int, float, str):
    n, gc_content, motif_seq = 0, 0.0, ""
    with open(filepath, 'r') as f:
        line1_data = f.readline().replace('\n', '').strip().split()
        n, gc_content = int(line1_data[0]), float(line1_data[1])
        motif_seq = f.readline().replace('\n', '').strip()
    return n, gc_content, motif_seq

def random_motif_prob(n_motifs: int, gc_content: float, target_seq: str):
    p = motif_prob(target_seq, gc_content)
    print(f"Prob for single seq - [{target_seq}]: {p}")
    return binom.cdf(n_motifs - 1, n_motifs, 1 - p)

if __name__ == '__main__':
    inpath = "./datasets/043.rstr.txt"
    n, gc, s = load_data(inpath)
    prob = random_motif_prob(n, gc, s)
    print(prob)
