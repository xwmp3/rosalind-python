# https://rosalind.info/problems/spec/
# Inferring Protein from Spectrum
# Script 053.spec.py created by minerw at 2022/09/20

from data import load_prot_mass_table
from utils import list_2_str


def load_data(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as f:
        mass_list = [float(line.strip()) for line in f]
    return mass_list


def mass_to_prot(target_mass: float, alpha: float = 0.0001) -> str:
    prot_ms = load_prot_mass_table()
    for prot_key in prot_ms.keys():
        if abs(target_mass - prot_ms[prot_key]) < alpha:
            # print(prot_key, target_mass)
            return prot_key


def prot_seq_from_specturm(spect_mass_list: list) -> list:
    res = []
    for i in range(1, len(spect_mass_list)):
        prt = mass_to_prot(spect_mass_list[i] - spect_mass_list[i - 1])
        res.append(prt)
    return res


if __name__ == "__main__":
    inpath = "./datasets/053.spec.in"
    ms = load_data(inpath)
    print(list_2_str(prot_seq_from_specturm(ms), sep=''))
