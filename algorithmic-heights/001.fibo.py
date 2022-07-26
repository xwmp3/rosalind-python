# https://rosalind.info/problems/fibo/

def fib(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def load_n(filepath: str):
    n = 0
    with open(filepath, 'r') as f:
        n = int(f.readline().replace('\n', '').strip())
    return n
    
if __name__ == "__main__":
    path = "./datasets/001.fibo.txt"
    n = load_n(path)
    print(fib(n))