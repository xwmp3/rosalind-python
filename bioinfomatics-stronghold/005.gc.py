# https://rosalind.info/problems/gc/

import numpy as np
from data import load_fasta


def gc_content(seq: str):
    count = 0
    for n in seq:
        if n == 'G' or n == 'C':
            count += 1
    return count / len(seq)


if __name__ == "__main__":
    path = 'datasets/005.gc.in'
    names, seqs = load_fasta(path)
    gc_content_list = [gc_content(seq) * 100 for seq in seqs]
    highest_index = np.argmax(gc_content_list)
    print(f"{names[highest_index]}\n{gc_content_list[highest_index]}")
