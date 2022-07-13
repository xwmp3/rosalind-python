# https://rosalind.info/problems/prtm/

def load_prot_mass_table(filepath: str) -> dict:
    mass_dict = {}
    with open(filepath, 'r') as f:
        for line in f.readlines():
            data = line.replace('\n', '').strip().split()
            mass_dict[data[0]] = float(data[1])
    return mass_dict

def load_data(filepath: str) -> str:
    seq: str = ""
    with open(filepath, 'r') as f:
        seq = f.readline().replace('\n', '').strip()
    return seq

def calc_prot_mass(seq: str, mass_dict: dict) -> float:
    return sum([mass_dict[item] for item in seq])

if __name__ == '__main__':
    path = "./datasets/020.prtm.txt"
    mass_table_path = "./datasets/020.monoisotopic-mass-table.txt"
    mass_dict = load_prot_mass_table(mass_table_path)
    print(mass_dict)
    prot_seq = load_data(path)
    print(prot_seq)
    print(calc_prot_mass(prot_seq, mass_dict))