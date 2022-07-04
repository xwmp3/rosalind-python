# https://rosalind.info/problems/fib/

def load_nk(filepath: str):
    n, k = 0, 0
    with open(filepath, 'r') as f:
        n, k = [int(d) for d in f.readline().replace('\n', '').strip().split()]
    print(f'n: {n}, k: {k}')
    return n, k

def rabbit_fib(n: int, k: int):
    if n == 1 or n == 2:
        return 1
    else:
        return rabbit_fib(n - 1, k) + k * rabbit_fib(n - 2, k)
    
if __name__ == "__main__":
    path = "./datasets/004.fib.txt"
    n, k = load_nk(path)
    print(rabbit_fib(n, k))