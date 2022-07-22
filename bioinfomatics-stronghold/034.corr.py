# https://rosalind.info/problems/corr/

# https://github.com/cdeterman/Rosalind/blob/master/034_CORR/034_CORR.py

from typing import List, Tuple
from collections import Counter

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

def load_data(filepath: str) -> list:
    return load_fasta(filepath)[1]

def dna_reverse_implement(seq: str):
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

def seqs_expansion(seqs: str):
    expand_seqs = []
    for seq in seqs:
        expand_seqs.append(seq)
        expand_seqs.append(dna_reverse_implement(seq))
    return expand_seqs

def hamming_distance(s1: str, s2: str):
    if len(s1) != len(s2):
        raise ValueError("Not the same length!")
    return sum(es1 != es2 for es1, es2 in zip(s1, s2))

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
    path = "./datasets/034.corr.txt"
    outpath = "./datasets/034.corr.out"
    seqs = load_data(path)
    expand_seqs = seqs_expansion(seqs)
    counter = Counter(expand_seqs)
    corr_seqs, incorr_seqs = correct_incorrect(counter, seqs)
    corrections = error_correction(corr_seqs, incorr_seqs)
    save_corrections(outpath, corrections)