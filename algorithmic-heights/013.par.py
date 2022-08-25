# https://rosalind.info/problems/par/
# 2-Way Partition

from utils import load_n_list, list_2_str, swap


def partition(arr: list, p: int, r: int) -> int:
    """
    快速排序中用于划分数组的函数
    对子数组arr[p..r]进行划分，用于分割的元素为arr[r]
    @param arr: 输入的原数组
    @param p: 子数组arr[p..r]的起始下标
    @param r: pivot元素的下标
    """
    pivot, ptr = arr[r], p
    for i in range(p, r):
        if arr[i] <= pivot:
            swap(arr, i, ptr)
            ptr += 1
    swap(arr, ptr, r)
    return ptr


if __name__ == "__main__":
    inpath = "./datasets/013.par.txt"
    outpath = "./datasets/013.par.out"
    n, x = load_n_list(inpath)
    print("Origin Data: \n{}".format(list_2_str(x)))
    x = x[1:] + [x[0]]
    partition(x, 0, n - 1)
    print("After Partition: \n{}".format(list_2_str(x)))
    with open(outpath, 'w') as f:
        f.write(list_2_str(x) + '\n')
    print("Save Results to {}".format(outpath))
