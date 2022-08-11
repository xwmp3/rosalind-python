# https://rosalind.info/problems/cc/

# Connected Components

'''
compute the number of connected components in a given `undirected` graph.
'''

from utils import load_graph_from_edge_list

# https://zhuanlan.zhihu.com/p/112771539
'''
Through DFS, we can get one of the connected components of a undirected graph every single search
So the times for dfs to look over the whole graph is also the number of connected components
'''
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
    
    cc = 0   
    for v in nodes:
        if v not in visited:
            cc += 1
            dfs(graph, v)
    
    return cc

if __name__ == "__main__":
    inpath = "./datasets/010.cc.txt"
    nodes, graph = load_graph_from_edge_list(inpath, undirected=True)
    print(connected_components(nodes, graph))
