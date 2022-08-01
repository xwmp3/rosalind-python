# https://rosalind.info/problems/grph/

import itertools

from data import load_fasta

def load_fasta_dict(filepath: str):
    fasta_dict = {}
    name_list, seq_list = load_fasta(filepath)
    for i, name in enumerate(name_list):
        fasta_dict[name] = seq_list[i]
    return fasta_dict

def is_overlap(s1: str, s2: str, k: int):
    return s1[-k:] == s2[:k]

def overlap_graph_edges(data: dict, overlap_k: int):
    edges = []
    for s1_name, s2_name in itertools.combinations(data, 2):
        s1, s2 = data[s1_name], data[s2_name]
        if is_overlap(s1, s2, overlap_k):
            edges.append((s1_name, s2_name))
        if is_overlap(s2, s1, overlap_k):
            edges.append((s2_name, s1_name))
    return edges
    
if __name__ == '__main__':
    inpath = './datasets/012.grph.txt'
    outpath = './datasets/012.grph.out'
    fasta_dict = load_fasta_dict(inpath)
    edges = overlap_graph_edges(fasta_dict, 3)
    with open(outpath, 'w') as f:
        for u, v in edges:
            f.write(f"{u} {v}\n")
    print(f"Save Results to {outpath}")