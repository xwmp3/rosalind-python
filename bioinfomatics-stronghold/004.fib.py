# https://rosalind.info/problems/fib/

def load_data(filepath: str) -> (int, int):
    with open(filepath, 'r') as f:
        n, k = [int(d) for d in f.readline().replace('\n', '').strip().split()]
    print(f'n: {n}, k: {k}')
    return n, k


def rabbit_fib_recursive(n: int, k: int):
    if n == 1 or n == 2:
        return 1
    else:
        return rabbit_fib_recursive(n - 1, k) + k * rabbit_fib_recursive(n - 2, k)


def rabbit_fib_non_recursive(n: int, k: int):
    fib_table = []
    for i in range(n):
        if i < 2:
            fib_table.append(1)
        else:
            fib_table.append(fib_table[-1] + k * fib_table[-2])
    return fib_table[n - 1]


if __name__ == "__main__":
    path = "./datasets/004.fib.txt"
    n, k = load_data(path)
    print(f"recursive:\t{rabbit_fib_recursive(n, k)}")
    print(f"non-recursive:\t{rabbit_fib_non_recursive(n, k)}")
