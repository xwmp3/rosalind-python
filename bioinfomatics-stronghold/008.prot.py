def load_rna_codon_table(filepath: str):
    rna_prot_map = {}
    with open(filepath, 'r') as f:
        for line in f.readlines():
            datas = line.replace('\n', '').strip().split()
            for i in range(4):
                rna_seq, prot = datas[2 * i], datas[2 * i + 1]
                rna_prot_map[rna_seq] = prot
    return rna_prot_map

def load_rna_seq(filepath: str):
    seq = ""
    with open(filepath, 'r') as f:
        seq = f.readline().replace('\n', '').strip()
    print(f'rna_seq: {seq}')
    return seq
    
def rna2prot(rna_prot_map: dict, seq: str):
    prot_list = []
    for i in range(int(len(seq) / 3)):
        prot = rna_prot_map[seq[3 * i: 3 * i + 3]]
        if prot == 'Stop': break
        prot_list.append(prot)
    return ''.join(prot_list)
    
if __name__ == "__main__":
    codon_table_path = "./datasets/008.rna-codon-table.txt"
    data_path = "./datasets/008.prot.txt"
    rna_prot_map = load_rna_codon_table(codon_table_path)
    rna_seq = load_rna_seq(data_path)
    print(rna2prot(rna_prot_map, rna_seq))