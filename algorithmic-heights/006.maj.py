# https://rosalind.info/problems/maj/

# Majority Element

"""
Count and get the majority element of list
-> 'majority' means the element appears in the list more than half the length of the list
"""

from collections import Counter


def load_data(filepath: str) -> (int, int, list):
    with open(filepath, 'r') as f:
        k, n = [int(item) for item in f.readline().replace('\n', '').strip().split()]
        num_list = [[int(item) for item in f.readline().replace('\n', '').strip().split()] for _ in range(k)]
    return k, n, num_list


def majority_element(x: list) -> int:
    counter = Counter(x)
    res = -1
    for key in counter.keys():
        count = counter[key]
        if count > len(x) / 2:
            res = key
    return res


if __name__ == '__main__':
    inpath = "./datasets/006.maj.txt"
    k, n, num_list = load_data(inpath)
    # print(k, n)
    # print(num_list)
    result = [majority_element(x) for x in num_list]
    print(' '.join([str(item) for item in result]))
