# https://rosalind.info/problems/grph/

import itertools

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
    path = './datasets/012.grph.txt'
    fasta_dict = load_fasta_dict(path)
    print(fasta_dict)
    edges = overlap_graph_edges(fasta_dict, 3)
    for u, v in edges:
        print(u, v)