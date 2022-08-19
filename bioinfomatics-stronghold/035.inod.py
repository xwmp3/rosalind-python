# https://rosalind.info/problems/inod/

def load_data(filepath: str):
    n = 0
    with open(filepath, 'r') as f:
        n = int(f.readline().replace('\n', '').strip())
    return n


def count_internal_nodes(n_leaves: int) -> int:
    return n_leaves - 2


if __name__ == '__main__':
    path = "./datasets/035.inod.txt"
    n = load_data(path)
    print(count_internal_nodes(n))
