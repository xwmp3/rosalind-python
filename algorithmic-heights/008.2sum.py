# https://rosalind.info/problems/2sum/

# 2SUM
from utils import timer, load_arrs, sort_with_pos
from itertools import permutations


@timer
def two_sum(x: list):
    sorted_x, sorted_pos = sort_with_pos(x)

    index_tuples = set()
    for i in range(0, len(sorted_x) - 1):
        if sorted_x[i] > 0:
            break
        if i > 0 and sorted_x[i] == sorted_x[i - 1]:
            continue

        target = - sorted_x[i]
        j = len(sorted_x) - 1

        while i < j:
            if len(index_tuples) == 1:
                break

            if sorted_x[j] == target:  # 第二个数等于target
                index_tuples.add((i, j))
                while i < j and sorted_x[j] == sorted_x[j - 1]:
                    j -= 1  # 跳过重复的数字
                i += 1
                j -= 1
            elif sorted_x[j] > target:  # 大于target，下标减一
                j -= 1
            else:  # 小于target，不存在这么个适合的数，直接退出吧
                break

    print(f"Get {len(index_tuples)} tuples")

    return [sorted([sorted_pos[index] + 1 for index in t]) for t in index_tuples]


@timer
def two_sum_in_double_for_loop(x: list):
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            # print(x[i], x[j], x[i] + x[j] == 0)
            if x[i] + x[j] == 0:
                return i + 1, j + 1
    return -1


@timer
def two_sum_with_perm(x: list):
    ret = -1
    for (i, j) in permutations([idx for idx in range(len(x))], r=2):
        if x[i] == -x[j]:
            ret = (i + 1, j + 1)
            break
    return ret


if __name__ == '__main__':
    inpath = "./datasets/008.2sum.txt"
    outpath = "./datasets/008.2sum.out"

    _, _, arrs = load_arrs(inpath)

    for arr in arrs:
        tuples = two_sum(arr)
        if len(tuples) != 0:  # check result
            pos1, pos2 = tuples[0]
            print(pos1, pos2, arr[pos1 - 1] + arr[pos2 - 1] == 0)

    res = [two_sum_with_perm(x) for x in arrs]

    outstr = ""
    for item in res:
        if item != -1:
            outstr += f"{' '.join([str(d) for d in item])}\n"
        else:
            outstr += f"{item}\n"
    print(outstr, end='')
    with open(outpath, 'w') as f:
        f.write(outstr)
    print(f"Save Result to {outpath}")
