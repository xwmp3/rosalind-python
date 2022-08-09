# https://rosalind.info/problems/bfs/

# Breadth-First Search

from utils import load_edge_list

def load_graph_from_edge_list(filepath: str):
    nodes, edges = load_edge_list(filepath)
    graph = {node:[] for node in nodes}
    for start_node, end_node in edges:
        graph[start_node].append(end_node)
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


if __name__ == '__main__':
    inpath = "./datasets/009.bfs.txt"
    outpath = "./datasets/009.bfs.out"
    nodes, graph = load_graph_from_edge_list(inpath)
    order, distance = breath_first_search(nodes, graph, 1)
    outstr = ' '.join([str(distance[key]) for key in distance.keys()])
    print(outstr)
    with open(outpath, 'w') as f:
        f.write(outstr + '\n')
    print(f"Save Result to {outpath}")
