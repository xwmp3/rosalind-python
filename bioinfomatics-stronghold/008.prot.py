# https://rosalind.info/problems/prot/

from data import load_rna_codon_table

def load_data(filepath: str):
    seq = ""
    with open(filepath, 'r') as f:
        seq = f.readline().replace('\n', '').strip()
    return seq
    
def rna2prot(rna_prot_map: dict, seq: str):
    prot_list = []
    for i in range(int(len(seq) / 3)):
        prot = rna_prot_map[seq[3 * i: 3 * i + 3]]
        if prot == 'Stop': break
        prot_list.append(prot)
    return ''.join(prot_list)
    
if __name__ == "__main__":
    data_path = "./datasets/008.prot.txt"
    rna_prot_map = load_rna_codon_table()
    rna_seq = load_data(data_path)
    print(rna2prot(rna_prot_map, rna_seq))