# https://rosalind.info/problems/rna/

from utils import dna_2_rna


def load_data(filepath: str) -> str:
    with open(filepath, 'r') as f:
        data = f.readline().replace('\n', '')
    return data


if __name__ == "__main__":
    inpath = "./datasets/002.rna.in"
    seq = load_data(inpath)
    print(dna_2_rna(seq))
