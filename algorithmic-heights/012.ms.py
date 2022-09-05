# https://rosalind.info/problems/ms/

# Merge Sort

from utils import load_n_list, list_2_str


# divide and conquer strategy
# merge sort algorithm implementation in Python
# 归并排序
def merge_sort(arr: list):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


if __name__ == "__main__":
    inpath = "./datasets/012.ms.in"
    outpath = "./datasets/012.ms.out"
    n, x = load_n_list(inpath)
    print("Origin Data: \n{}".format(list_2_str(x)))
    merge_sort(x)
    print("Sorted Data: \n{}".format(list_2_str(x)))
    with open(outpath, 'w') as f:
        f.write(f"{list_2_str(x)}\n")
    print("Save Results to {}".format(outpath))
