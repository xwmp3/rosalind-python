import numpy as np


def load_edge_list(filepath: str) -> (list, list):
    n, m, nodes, edges = 0, 0, [], []
    with open(filepath, 'r') as f:
        # n->number of nodes, m->number of edges
        n, m = [int(item) for item in f.readline().replace('\n', '').strip().split()]
        for _ in range(m):  # read edges
            start_node, end_node = [int(item) for item in f.readline().replace('\n', '').strip().split()]
            edges.append((start_node, end_node))
        nodes = [item for item in range(1, n + 1)]
    print(f"Load {len(edges)} edges, {len(nodes)} nodes from {filepath}")
    return nodes, edges


def load_graph_from_edge_list(filepath: str, undirected: bool = False):
    nodes, edges = load_edge_list(filepath)
    graph = {node: [] for node in nodes}
    for start_node, end_node in edges:
        graph[start_node].append(end_node)
        if undirected:
            graph[end_node].append(start_node)
    return nodes, graph


def breath_first_search(nodes: list, graph: dict, start_node):
    if start_node not in nodes:
        return
        # init queue, order and distance dict
    queue, order = [], []
    distance = {node: 0 for node in nodes}
    queue.append(start_node)
    order.append(start_node)
    # start search
    while queue:
        v = queue.pop(0)
        for n in graph[v]:
            if n not in order:
                distance[n] = distance[v] + 1
                order.append(n)
                queue.append(n)
    # mark unreachable node's distance as -1
    for n in nodes:
        if n not in order:
            distance[n] = -1
    return order, distance


def degree_array(nodes: list, edges: list) -> list:
    da_dict = {node: 0 for node in nodes}
    for start_node, end_node in edges:
        da_dict[start_node] += 1
        da_dict[end_node] += 1
    return [da_dict[node] for node in nodes]
