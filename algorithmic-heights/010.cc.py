# https://rosalind.info/problems/cc/

# Connected Components

"""
Use depth-first search to compute the number of connected components in a given undirected graph.
"""
from utils import load_graph_from_edge_list


# https://zhuanlan.zhihu.com/p/112771539
def connected_components(nodes, graph):
    visited = []
    stack = []

    def dfs(graph: dict, v):
        stack.append(v)
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
            else:
                continue
            for neighbor in graph[node]:
                stack.append(neighbor)

    n_visits = 0  # one visit -> one connected component
    for v in nodes:
        if v not in visited:
            n_visits += 1
            dfs(graph, v)

    return n_visits


if __name__ == "__main__":
    inpath = "./datasets/010.cc.txt"
    nodes, graph = load_graph_from_edge_list(inpath, undirected=True)
    cc = connected_components(nodes, graph)
    print(f"There're {cc} connected components in graph.")
