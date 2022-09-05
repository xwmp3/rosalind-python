# https://rosalind.info/problems/ins/

# Insertion Sort

"""
Count the number of swaps performed be INSERTION SORT algorithm
"""
from utils import load_n_list, swap


def insertion_sort_with_swap_counter(arr: list) -> (list, int):
    swap_count = 0
    for i in range(1, len(arr)):
        k = i
        while k > 0 and arr[k] < arr[k - 1]:
            swap_count += 1
            swap(arr, k - 1, k)
            k = k - 1
    return arr, swap_count


if __name__ == "__main__":
    inpath = "./datasets/004.ins.in"
    n, x = load_n_list(inpath)
    print(n, x)
    x_new, count = insertion_sort_with_swap_counter(x)
    print(count)
