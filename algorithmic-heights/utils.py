def timer(func):
    def func_wrapper(*args, **kwargs):
        from time import time
        time_start = time()
        result = func(*args, **kwargs)
        time_end = time()
        print('{0} cost time {1} s'.format(func.__name__, time_end - time_start))

        return result

    return func_wrapper


def load_edge_list(filepath: str) -> (list, list):
    n, m, nodes, edges = 0, 0, [], []
    with open(filepath, 'r') as f:
        # n->number of nodes, m->number of edges
        n, m = [int(item) for item in f.readline().strip().split()]
        for _ in range(m):  # read edges
            start_node, end_node = [int(item) for item in f.readline().strip().split()]
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


def load_n_list(filepath: str) -> (int, list):
    with open(filepath, 'r', encoding='utf-8') as f:
        n_elems = int(f.readline().strip())
        elems = [int(item) for item in f.readline().strip().split()]
    return n_elems, elems


def load_arrs(filepath: str) -> (int, int, list):
    with open(filepath, 'r', encoding='utf-8') as f:
        n_arrs, arr_len = [int(item) for item in f.readline().strip().split()]
        arrs = [[int(elem) for elem in f.readline().strip().split()] for _ in range(n_arrs)]
    print(f"Load {n_arrs} lists, each list has {arr_len} elems")
    return n_arrs, arr_len, arrs


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


def list_2_str(x: list, sep: str = ' '):
    return sep.join([str(item) for item in x])


def swap(arr: list, pos1: int, pos2: int):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]


def sort_with_pos(x: list) -> (list, list):
    elem_pos_tuples = [(x[pos], pos) for pos in range(len(x))]
    elem_pos_tuples = sorted(elem_pos_tuples, key=lambda t: t[0])

    sorted_x = [t[0] for t in elem_pos_tuples]
    sorted_pos = [t[1] for t in elem_pos_tuples]

    return sorted_x, sorted_pos
