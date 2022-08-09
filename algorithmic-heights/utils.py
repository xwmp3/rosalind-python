import numpy as np

def load_edge_list(filepath: str) -> (int, int, list):
    n, m, edges = 0, 0, []
    with open(filepath, 'r') as f:
        n, m = [int(item) for item in f.readline().replace('\n', '').strip().split()]
        for _ in range(m):
            start_node, end_node = [int(item) for item in f.readline().replace('\n', '').strip().split()]
            edges.append((start_node, end_node))
    return n, m, edges

