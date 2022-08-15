# https://rosalind.info/problems/dna/

from utils import count_nucleotides


def load_data(filepath: str) -> str:
    with open(filepath, 'r') as f:
        seq = f.readline().replace('\n', '')
    return seq


if __name__ == "__main__":
    inpath = './datasets/001.dna.txt'
    seq = load_data(inpath)
    print(len(seq))
    print(' '.join([str(count) for count in count_nucleotides(seq)]))
