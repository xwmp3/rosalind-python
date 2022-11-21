# https://rosalind.info/problems/revc/

from utils import reverse_complement


def load_data(filepath: str):
    with open(filepath, 'w', encoding='utf-8') as f:
        seq = f.readline().strip()
    return seq


if __name__ == "__main__":
    inpath = './datasets/003.revc.in'
    dna_seq = load_data(inpath)
    print(reverse_complement(dna_seq))
