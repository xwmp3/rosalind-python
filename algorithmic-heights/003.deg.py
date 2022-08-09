# https://rosalind.info/problems/deg/

# Degree Array

from utils import load_edge_list

def degree_array(n_nodes: int, edges: list):
    d_a = [0]*n_nodes
    for start_node, end_node in edges:
        d_a[start_node - 1] += 1
        d_a[end_node - 1] += 1
    return d_a

if __name__ == "__main__":
    inpath = "./datasets/003.deg.txt"
    outpath = "./datasets/003.deg.out"
    n, m, edges = load_edge_list(inpath)
    results = degree_array(n, edges)
    with open(outpath, 'w') as f:
        f.write(' '.join([str(i) for i in results]) + '\n')
    print(f"Save Results to {outpath}")
