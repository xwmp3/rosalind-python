# https://rosalind.info/problems/ddeg/

# Double-Degree Array

from utils import load_edge_List

def degree_array(n_nodes: int, edges: list):
    d_a = [0]*n_nodes
    for start_node, end_node in edges:
        d_a[start_node - 1] += 1
        d_a[end_node - 1] += 1
    return d_a

def neighbor_list(n_nodes: int, edges: list):
    res = [set() for _ in range(n_nodes)]
    for start_node, end_node in edges:
        res[start_node - 1].add(end_node - 1)
        res[end_node - 1].add(start_node - 1)
    return [list(s) for s in res]

def double_degree_array(degree_array: list, neighbor_list: list):
    res = []
    for i in range(len(degree_array)):
        res.append(sum([degree_array[neighbor_index] for neighbor_index in neighbor_list[i]]))
    return res

if __name__ == "__main__":
    inpath = "./datasets/005.ddeg.txt"
    outpath = "./datasets/005.ddeg.out"
    n, m, edges = load_edge_List(inpath)
    d_a = degree_array(n, edges)
    n_l = neighbor_list(n, edges)
    results = double_degree_array(d_a, n_l)
    with open(outpath, 'w') as f:
        f.write(' '.join([str(i) for i in results]) + '\n')
    print(f"Save Results to {outpath}")