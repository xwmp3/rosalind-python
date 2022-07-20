# https://rosalind.info/problems/tree/

def load_data(filepath: str):
    num_nodes, edges = 0, []
    with open(filepath, 'r') as f:
        num_nodes = int(f.readline().replace('\n', '').strip())
        for line in f.readlines():
            node1, node2 = [int(d) for d in line.replace('\n', '').strip().split()]
            edges.append((node1, node2))
    return num_nodes, edges

def tree_need_edges(n_nodes: int, edges: list) -> int:
    return n_nodes - 1 - len(edges) # n_nodes = n_edges + 1
    
if __name__ == '__main__':
    path = "./datasets/032.tree.txt"
    num_nodes, edges = load_data(path)
    print(num_nodes, edges)
    print(tree_need_edges(num_nodes, edges))