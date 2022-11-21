# https://rosalind.info/problems/conv/
# Comparing Spectra with the Spectral Convolution
# Script 055.conv.py created by minerw at 2022/10/13

from collections import Counter


def load_data(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as f:
        spectra1 = [float(item) for item in f.readline().strip().split()]
        spectra2 = [float(item) for item in f.readline().strip().split()]
    return spectra1, spectra2


def spectra_comparation(spectra1: list, spectra2: list, n_round: int = 5):
    convs = []
    """
    简化的闵可夫斯基差（Minkowski Difference）
    A−B={c|c+B⊆A}
    http://twistedoakstudios.com/blog/Post554_minkowski-sums-and-differences
    """
    for i in range(len(spectra1)):
        for j in range(len(spectra2)):
            convs.append(round(spectra1[i] - spectra2[j], n_round))
    max_count_x, n_count = Counter(convs).most_common()[0]
    return n_count, max_count_x


if __name__ == "__main__":
    inpath = "./datasets/055.conv.in"

    s1, s2 = load_data(inpath)
    n, x = spectra_comparation(s1, s2)
    print(n)
    print(x)
