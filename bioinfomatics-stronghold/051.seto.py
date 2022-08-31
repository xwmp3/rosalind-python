# https://rosalind.info/problems/seto/

# Introduction to Set Operations

from utils import list_2_str

def load_data(filepath: str) -> (set, set, set):
    with open(filepath, 'r', encoding='utf-8') as f:
        n = int(f.readline().replace('\n', '').strip())
        set_u = set(range(1, n + 1))
        set_a = set([int(item) for item in f.readline().replace('\n', '').strip()[1:-1].split(',')])
        set_b = set([int(item) for item in f.readline().replace('\n', '').strip()[1:-1].split(',')])

    print(f"Set U: {set_u}\nSet A: {set_a}\nSet B: {set_b}")

    return set_u, set_a, set_b


def set_operations(set_u: set, set_a: set, set_b: set):
    return set_a | set_b, set_a & set_b, set_a - set_b, set_b - set_a, set_u - set_a, set_u - set_b


if __name__ == "__main__":
    inpath = "./datasets/051.seto.txt"
    outpath = "./datasets/051.seto.out"
    outfile = open(outpath, 'w', encoding='utf-8')
    u, a, b = load_data(inpath)
    for item_set in set_operations(u, a, b):
        print(item_set)
        outfile.write(str(item_set) + '\n')
    outfile.close()
