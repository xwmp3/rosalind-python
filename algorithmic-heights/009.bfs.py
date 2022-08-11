# https://rosalind.info/problems/bfs/

# Breadth-First Search

from utils import load_graph_from_edge_list, breath_first_search

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
