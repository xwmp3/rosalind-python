# https://rosalind.info/problems/tran/

from data import load_fasta


def load_data(filepath: str) -> tuple:
    return load_fasta(filepath)[1]


def trans_ratio(s1: str, s2: str) -> float:
    transitions = ['AG', 'GA', 'CT', 'TC']
    transversions = ['AC', 'CA', 'AT', 'TA', 'CG', 'GC', 'GT', 'TG']
    transition_count, transversion_count = 0, 0
    for i in range(0, len(s1)):
        temp = f'{s1[i]}{s2[i]}'
        if temp in transitions:
            transition_count += 1
        elif temp in transversions:
            transversion_count += 1
    return transition_count / transversion_count


if __name__ == '__main__':
    path = "datasets/031.tran.in"
    s1, s2 = load_data(path)
    print(trans_ratio(s1, s2))
