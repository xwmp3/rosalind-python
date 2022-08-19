# https://rosalind.info/problems/2sum/

# 2SUM

def load_data(filepath: str) -> list:
    with open(filepath, 'r') as f:
        k, n = [int(item) for item in f.readline().replace('\n', '').strip().split()]
        arrays = []
        for i in range(k):
            arrays.append([int(item) for item in f.readline().replace('\n', '').strip().split()])
    return arrays


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


if __name__ == '__main__':
    inpath = "./datasets/008.2sum.txt"
    outpath = "./datasets/008.2sum.out"

    Xs = load_data(inpath)

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
