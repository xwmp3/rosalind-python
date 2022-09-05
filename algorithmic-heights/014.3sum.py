# https://rosalind.info/problems/3sum/

# 3SUM

from utils import timer, load_arrs, list_2_str, sort_with_pos


# https://www.cnblogs.com/grandyang/p/4481576.html
@timer
def three_sum(x: list) -> list:
    sorted_x, sorted_pos = sort_with_pos(x)  # 带着原本的下标一起排序

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
                break  # 在找到第一个结果之后就直接break

            if sorted_x[i] + sorted_x[j] == target:  # 等于目标
                index_triplets.add((k, i, j))
                # 跳过重复的
                while i < j and sorted_x[i] == sorted_x[i + 1]:
                    i += 1
                while i < j and sorted_x[j] == sorted_x[j - 1]:
                    j -= 1
                i += 1
                j -= 1
            elif sorted_x[i] + sorted_x[j] < target:  # 小于目标，说明第二个数小了，下标加一
                i += 1
            else:  # 大于目标，说明第三个数大了，下标减一
                j -= 1

    print(f"Get {len(index_triplets)} triplets")

    return [sorted([sorted_pos[index] + 1 for index in triplet]) for triplet in index_triplets]  # 转换到原本的下标


if __name__ == "__main__":
    inpath = "./datasets/014.3sum.in"
    outpath = "./datasets/014.3sum.out"

    _, _, arrs = load_arrs(inpath)

    os = open(outpath, 'w', encoding='utf-8')

    for arr in arrs:
        triplets = three_sum(arr)
        if len(triplets) == 0:
            os.write('-1\n')
        else:
            os.write(f"{list_2_str(triplets[0])}\n")

    os.close()
    print(f"Save Results to {outpath}")
