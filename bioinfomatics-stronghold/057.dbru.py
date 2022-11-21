# https://rosalind.info/problems/dbru/
# Constructing a De Bruijn Graph
# Script 057.dbru.py created by minerw at 2022/10/26

from utils import reverse_complement


def load_data(filepath: str) -> set:
    with open(filepath, 'r', encoding='utf-8') as f:
        seqs = set(line.strip() for line in f)
    return seqs


def get_k_mers(seq: str, k: int) -> list:
    assert k <= len(seq), f'k({k}) is not allowed to bigger than seq length({len(seq)})'
    if k == len(seq):
        return [seq]
    else:
        return [seq[i: i + k] for i in range(len(seq) - k + 1)]


def make_de_bruijn(seqs: set) -> list:
    rc_seqs = set(reverse_complement(seq) for seq in seqs)
    union_seqs = seqs | rc_seqs
    return [get_k_mers(s, len(s) - 1) for s in union_seqs]


def save_de_bruijn(filepath: str, edges: list):
    with open(filepath, 'w', encoding='utf-8') as f:
        for mer1, mer2 in edges:
            f.write(f'({mer1}, {mer2})\n')
    print(f"De Bruijn Graph with {len(edges)} edges saved to {filepath}")


if __name__ == "__main__":
    inpath = "./datasets/057.dbru.in"
    outpath = "./datasets/057.dbru.out"

    dna_seqs = load_data(inpath)
    db_graph = make_de_bruijn(dna_seqs)
    for m1, m2 in db_graph:
        print(f'({m1}, {m2})')
    save_de_bruijn(outpath, db_graph)
