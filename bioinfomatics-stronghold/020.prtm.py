# https://rosalind.info/problems/prtm/

from data import load_prot_mass_table


def load_data(filepath: str) -> str:
    seq: str = ""
    with open(filepath, 'r') as f:
        seq = f.readline().replace('\n', '').strip()
    return seq


def calc_prot_mass(seq: str, mass_dict: dict) -> float:
    return sum([mass_dict[item] for item in seq])


if __name__ == '__main__':
    path = "./datasets/020.prtm.txt"
    mass_dict = load_prot_mass_table()
    prot_seq = load_data(path)
    print(calc_prot_mass(prot_seq, mass_dict))
