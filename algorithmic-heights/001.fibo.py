# https://rosalind.info/problems/fibo/

"""
Get Fibonacci Number in Recursive
"""


def fib_recursive(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


def load_n(filepath: str):
    with open(filepath, 'r') as f:
        n = int(f.readline().replace('\n', '').strip())
    return n


if __name__ == "__main__":
    path = "./datasets/001.fibo.txt"
    n = load_n(path)
    print(fib_recursive(n))
