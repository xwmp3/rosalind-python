# https://rosalind.info/problems/seto/

# Introduction to Set Operations


def load_data(filepath: str) -> (set, set, set):
    with open(filepath, 'r', encoding='utf-8') as f:
        n = int(f.readline().replace('\n', '').strip())
        set_u = set(range(1, n + 1))
        set_a = set([int(item) for item in f.readline().replace('\n', '').strip()[1:-1].split(',')])
        set_b = set([int(item) for item in f.readline().replace('\n', '').strip()[1:-1].split(',')])

    # print(f"Set U: {set_u}\nSet A: {set_a}\nSet B: {set_b}")
    return set_u, set_a, set_b


def set_operations(set_u: set, set_a: set, set_b: set):
    # 并集、交集、集合减法、补集
    return set_a | set_b, set_a & set_b, set_a - set_b, set_b - set_a, set_u - set_a, set_u - set_b


if __name__ == "__main__":
    inpath = "./datasets/051.seto.in"
    outpath = "./datasets/051.seto.out"
    u, a, b = load_data(inpath)
    with open(outpath, 'w', encoding='utf-8') as outfile:
        for item_set in set_operations(u, a, b):
            outfile.write(str(item_set) + '\n')
    print(f"Save Results to {outpath}")
