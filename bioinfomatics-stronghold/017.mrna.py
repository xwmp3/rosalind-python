# https://rosalind.info/problems/mrna/

def load_data(filepath: str):
    data = ""
    with open(filepath, 'r') as f:
        data = f.readline().replace('\n', '').strip()
    return data

def load_rna_codon_table(filepath: str):
    rna_prot_map = {}
    with open(filepath, 'r') as f:
        for line in f.readlines():
            datas = line.replace('\n', '').strip().split()
            for i in range(4):
                rna_seq, prot = datas[2 * i], datas[2 * i + 1]
                rna_prot_map[rna_seq] = prot
    return rna_prot_map

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

def infer_mrna_num(prot_seq: str, amino_list: list, num_list: list):
    total = 1
    for n in prot_seq:
        index = amino_list.index(n)
        num = num_list[index]
        total *= num
    total *= num_list[amino_list.index('Stop')]
    return total % 1000000

if __name__ == '__main__':
    codon_table_path = "./datasets/008.rna-codon-table.txt"
    path = './datasets/017.mrna.txt'
    prot_seq = load_data(path)
    print(prot_seq)
    aminos, nums = rc_table_2_num_reverse(load_rna_codon_table(codon_table_path))
    print(infer_mrna_num(prot_seq, aminos, nums))