# https://rosalind.info/problems/2sum/

# 2SUM
from utils import timer, load_arrs, sort_with_pos


@timer
def two_sum_indices(x: list):
    """
    iterate over a two-dimensional array
    @param x:
    @return:
    """
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            # print(x[i], x[j], x[i] + x[j] == 0)
            if x[i] + x[j] == 0:
                return i + 1, j + 1
    return -1


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

            if sorted_x[j] == target:  # 第二个数要么等于目标数，要么大于目标数
                index_tuples.add((i, j))
                while i < j and sorted_x[j] == sorted_x[j - 1]:
                    j -= 1
                i += 1
                j -= 1
            else:
                j -= 1

    print(f"Get {len(index_tuples)} tuples")

    return [sorted([sorted_pos[index] + 1 for index in t]) for t in index_tuples]


if __name__ == '__main__':
    inpath = "./datasets/008.2sum.txt"
    outpath = "./datasets/008.2sum.out"

    _, _, Xs = load_arrs(inpath)

    for x in Xs:
        tuples = two_sum(x)

        if len(tuples) != 0:
            pos1, pos2 = tuples[0]
            print(x[pos1 - 1] + x[pos2 - 1])

    res = [two_sum_indices(x) for x in Xs]

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
