# https://rosalind.info/problems/hamm/

# Counting Point Mutations

from typing import Tuple

from utils import hamming_distance


def load_data(filepath: str) -> Tuple[str, str]:
    with open(filepath, 'r') as f:
        s1 = f.readline().replace('\n', '').strip()
        s2 = f.readline().replace('\n', '').strip()
    return s1, s2


if __name__ == "__main__":
    path = 'datasets/006.hamm.in'
    s1, s2 = load_data(path)
    print(s1, s2)
    print(hamming_distance(s1, s2))
