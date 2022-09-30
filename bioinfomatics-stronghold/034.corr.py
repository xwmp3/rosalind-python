# https://rosalind.info/problems/corr/

# https://github.com/cdeterman/Rosalind/blob/master/034_CORR/034_CORR.py

from typing import List, Tuple
from collections import Counter

from data import load_fasta
from utils import hamming_distance, dna_reverse_implement


def load_data(filepath: str):
    return load_fasta(filepath)[1]


def seqs_expansion(seqs: str):
    expand_seqs = []
    for seq in seqs:
        expand_seqs.append(seq)
        expand_seqs.append(dna_reverse_implement(seq))
    return expand_seqs


def correct_incorrect(counts, orig_seqs):
    correct = []
    incorrect = []
    for s in counts:
        if counts[s] >= 2:
            correct.append(s)
        elif s in orig_seqs:
            incorrect.append(s)
    return correct, incorrect


def error_correction(corrs: list, incorrs: list):
    correct_tuples = []
    for s1 in incorrs:
        for s2 in corrs:
            if hamming_distance(s1, s2) == 1:
                correct_tuples.append((s1, s2))
    return correct_tuples


def save_corrections(filepath: str, corrections: List[Tuple]):
    out = open(filepath, 'w')
    for s1, s2 in corrections:
        out.write(f"{s1}->{s2}\n")
    out.close()
    print(f"Save result to {filepath}.")


if __name__ == '__main__':
    path = "datasets/034.corr.in"
    outpath = "./datasets/034.corr.out"
    seqs = load_data(path)
    expand_seqs = seqs_expansion(seqs)
    counter = Counter(expand_seqs)
    corr_seqs, incorr_seqs = correct_incorrect(counter, seqs)
    corrections = error_correction(corr_seqs, incorr_seqs)
    save_corrections(outpath, corrections)
