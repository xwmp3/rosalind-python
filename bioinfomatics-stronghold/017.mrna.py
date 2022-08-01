# https://rosalind.info/problems/mrna/

from data import load_rna_codon_table

def load_data(filepath: str):
    data = ""
    with open(filepath, 'r') as f:
        data = f.readline().replace('\n', '').strip()
    return data

def rc_table_2_num_reverse(table_dict: dict):
    amino_list, num_list = [], []
    for key in table_dict.keys():
        amino = table_dict[key]
        if amino not in amino_list:
            amino_list.append(amino)
            num_list.append(1)
        else:
            num_list[amino_list.index(amino)] += 1
    return amino_list, num_list

def infer_mrna_num(prot_seq: str, amino_list: list, num_list: list, module: int=10**6):
    total = 1
    for n in prot_seq:
        index = amino_list.index(n)
        num = num_list[index]
        total *= num
    total *= num_list[amino_list.index('Stop')]
    return total % module

if __name__ == '__main__':
    path = './datasets/017.mrna.txt'
    prot_seq = load_data(path)
    print(prot_seq)
    aminos, nums = rc_table_2_num_reverse(load_rna_codon_table())
    print(infer_mrna_num(prot_seq, aminos, nums))