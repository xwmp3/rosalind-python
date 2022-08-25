# https://rosalind.info/problems/maj/

# Majority Element

"""
Count and get the majority element of list
-> 'majority' means the element appears in the list more than half the length of the list
"""

from collections import Counter

from utils import load_arrs


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
    k, n, num_list = load_arrs(inpath)
    # print(k, n)
    # print(num_list)
    result = [majority_element(x) for x in num_list]
    print(' '.join([str(item) for item in result]))
