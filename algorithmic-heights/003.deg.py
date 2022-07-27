# https://rosalind.info/problems/deg/

# Degree Array

def load_edge_List(filepath: str) -> (int, int, list):
    n, m, edges = 0, 0, []
    with open(filepath, 'r') as f:
        n, m = [int(item) for item in f.readline().replace('\n', '').strip().split()]
        for _ in range(m):
            start_node, end_node = [int(item) for item in f.readline().replace('\n', '').strip().split()]
            edges.append((start_node, end_node))
    return n, m, edges

def degree_array(n_nodes: int, edges: list):
    d_a = [0]*n_nodes
    for start_node, end_node in edges:
        d_a[start_node - 1] += 1
        d_a[end_node - 1] += 1
    return d_a

if __name__ == "__main__":
    inpath = "./datasets/003.deg.txt"
    outpath = "./datasets/003.deg.out"
    n, m, edges = load_edge_List(inpath)
    results = degree_array(n, edges)
    with open(outpath, 'w') as f:
        f.write(' '.join([str(i) for i in results]) + '\n')
    print(f"Save Results to {outpath}")