# https://rosalind.info/problems/iev/

import numpy as np


def load_data(filepath: str):
    with open(filepath, 'r') as f:
        n_list = [int(d) for d in f.readline().replace('\n', '').strip().split()]
    print(n_list)
    return n_list


def expected_p_for_dominant_offspring(pair_nums: list):
    # AA-AA \ AA-Aa \ AA-aa \ Aa-Aa \ Aa-aa \ aa-aa
    dedicated_p_value = [1, 1, 1, 0.75, 0.5, 0]
    return np.sum([2 * num * dedicated_p_value[i] for i, num in enumerate(pair_nums)])


if __name__ == '__main__':
    path = './datasets/013.iev.txt'
    pair_nums = load_data(path)
    print(expected_p_for_dominant_offspring(pair_nums))
