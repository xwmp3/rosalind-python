# https://rosalind.info/problems/lcsq/

# Finding a Shared Spliced Motif

from utils import load_fasta

def load_data(filepath: str) -> (str, str):
    s1, s2 = load_fasta(filepath)[1]
    return s1, s2

# https://atqingke.com/index.php/archives/564/
import numpy as np
def longest_common_subseq(s1: str, s2: str):
    len1, len2 = len(s1), len(s2)
    lcs = np.zeros((len1 + 1, len2 + 1))
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if s1[i-1] == s2[j-1]:
                lcs[i][j] = lcs[i-1][j-1] + 1
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
    
    res_seq = ""
    i, j = len1, len2
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            res_seq += s1[i-1]
            i -= 1
            j -= 1
        else:
            if lcs[i][j-1] > lcs[i-1][j]:
                j -= 1
            elif lcs[i][j-1] < lcs[i-1][j]:
                i -= 1
            else:
                j -= 1
    
    return res_seq[::-1]

if __name__ == '__main__':
    inpath = "./datasets/038.lcsq.txt"
    outpath = "./datasets/038.lcsq.out"
    seq1, seq2 = load_data(inpath)
    lcs = longest_common_subseq(seq1, seq2)
    with open(outpath, 'w') as f:
        f.write(f"{lcs}\n")
    print(f"Save Results to {outpath}")

