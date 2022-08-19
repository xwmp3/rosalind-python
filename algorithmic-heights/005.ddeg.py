# https://rosalind.info/problems/ddeg/

# Double-Degree Array

from utils import load_edge_list, degree_array


def neighbor_list(nodes: list, edges: list):
    nl_dict = {node: set() for node in nodes}
    for start_node, end_node in edges:
        nl_dict[start_node].add(end_node)
        nl_dict[end_node].add(start_node)
    return [list(nl_dict[node]) for node in nodes]


def double_degree_array(nodes: list, degree_array: list, neighbor_list: list):
    dd_a = []
    for i in range(len(nodes)):
        dd_a.append(sum([degree_array[nodes.index(neighbor)] for neighbor in neighbor_list[i]]))
    return dd_a


if __name__ == "__main__":
    inpath = "./datasets/005.ddeg.txt"
    outpath = "./datasets/005.ddeg.out"
    nodes, edges = load_edge_list(inpath)
    d_a = degree_array(nodes, edges)
    n_l = neighbor_list(nodes, edges)
    dd_a = double_degree_array(nodes, d_a, n_l)
    with open(outpath, 'w') as f:
        outstr = ' '.join([str(i) for i in dd_a])
        print(outstr)
        f.write(outstr + '\n')
    print(f"Save Results to {outpath}")
