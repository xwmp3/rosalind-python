import numpy as np

def load_edge_list(filepath: str) -> (list, list):
    n, m, nodes, edges = 0, 0, [], []
    with open(filepath, 'r') as f:
        # n->number of nodes, m->number of edges
        n, m = [int(item) for item in f.readline().replace('\n', '').strip().split()]
        for _ in range(m): # read edges
            start_node, end_node = [int(item) for item in f.readline().replace('\n', '').strip().split()]
            edges.append((start_node, end_node))
        nodes = [item for item in range(1, n+1)]
    print(f"Load {len(edges)} edges, {len(nodes)} nodes from {filepath}")
    return nodes, edges

def degree_array(nodes: list, edges: list):
    da_dict = {node:0 for node in nodes}
    for start_node, end_node in edges:
        da_dict[start_node] += 1
        da_dict[end_node] += 1
    return [da_dict[node] for node in nodes]
