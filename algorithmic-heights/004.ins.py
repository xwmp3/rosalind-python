# https://rosalind.info/problems/ins/

# Insertion Sort

"""
Count the number of swaps performed be INSERTION SORT algorithm
"""


def load_data(filepath: str) -> (int, list):
    with open(filepath, 'r') as f:
        n = int(f.readline().replace('\n', '').strip())
        x = [int(item) for item in f.readline().replace('\n', '').strip().split()]
    return n, x


def swap(x: list, index1: int, index2: int):
    temp = x[index1]
    x[index1] = x[index2]
    x[index2] = temp


def insertion_sort_with_swap_counter(x: list) -> (list, int):
    swap_count = 0
    for i in range(1, len(x)):
        k = i
        while k > 0 and x[k] < x[k - 1]:
            swap_count += 1
            swap(x, k - 1, k)
            k = k - 1
    return x, swap_count


if __name__ == "__main__":
    inpath = "./datasets/004.ins.txt"
    n, x = load_data(inpath)
    print(n, x)
    x_new, count = insertion_sort_with_swap_counter(x)
    print(count)
