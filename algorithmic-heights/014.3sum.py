# https://rosalind.info/problems/3sum/

# 3SUM

from utils import load_arrs, list_2_str


# https://www.cnblogs.com/grandyang/p/4481576.html
def three_sum(x: list) -> list:
    elem_pos_tuples = [(x[pos], pos) for pos in range(len(x))]  # 本题需要输出原数组中的pos triplets，所以给他先记下
    elem_pos_tuples = sorted(elem_pos_tuples, key=lambda t: t[0])  # 输入的数组中肯定有正数和负数，排序后负数在前面

    # 排序完了拆开
    sorted_x = [t[0] for t in elem_pos_tuples]
    sorted_pos = [t[1] for t in elem_pos_tuples]

    index_triplets = set()
    for k in range(0, len(sorted_x) - 2):
        if sorted_x[k] > 0:  # 从头开始遍历的话，固定第一个数为负数，遍历到正数即结束
            break  # 因为后面全是正数，三个正数和不可能为0
        if k > 0 and sorted_x[k] == sorted_x[k - 1]:
            continue  # 跳过重复的

        target = - sorted_x[k]  # 后两个数之和的目标为第一个数的相反数
        i = k + 1  # 一个从前往后遍历
        j = len(sorted_x) - 1  # 一个从后往前遍历，避免重复

        while i < j:
            if len(index_triplets) == 1:  # 本题不需要找出所有triplets
                break

            if sorted_x[i] + sorted_x[j] == target:  # 符合条件
                index_triplets.add((k, i, j))
                # 跳过重复的
                while i < j and sorted_x[i] == sorted_x[i - 1]:
                    i += 1
                while i < j and sorted_x[j] == sorted_x[j - 1]:
                    j -= 1
                i += 1
                j -= 1
            elif sorted_x[i] + sorted_x[j] < target:  # 加起来小于目标，说明第二个数小了，下标加一
                i += 1
            else:  # 小于目标，说明第三个数大了，下标减一
                j -= 1

    print(f"Get {len(index_triplets)} triplets")

    return [sorted([sorted_pos[index] + 1 for index in triplet]) for triplet in index_triplets]  # 转换到原本的下标


if __name__ == "__main__":
    inpath = "./datasets/014.3sum.txt"
    outpath = "./datasets/014.3sum.out"

    os = open(outpath, 'w', encoding='utf-8')

    _, _, arrs = load_arrs(inpath)

    for arr in arrs:
        triplets = three_sum(arr)
        # print(triplets)
        if len(triplets) == 0:
            os.write('-1\n')
        else:
            os.write(f"{list_2_str(triplets[0])}\n")

    print(f"Save Results to {outpath}")
