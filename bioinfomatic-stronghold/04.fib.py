def rabbit_fib(n: int, k: int):
    if n == 1 or n == 2:
        return 1
    else:
        return rabbit_fib(n - 1, k) + k * rabbit_fib(n - 2, k)
    
if __name__ == "__main__":
    n = 5
    k = 3
    print(rabbit_fib(n, k))