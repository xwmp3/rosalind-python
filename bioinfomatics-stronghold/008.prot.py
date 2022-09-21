# https://rosalind.info/problems/prot/

from utils import rna_2_protein, list_2_str


def load_data(filepath: str):
    with open(filepath, 'r') as f:
        seq = f.readline().replace('\n', '').strip()
    return seq


def rna2prot(rna_prot_map: dict, seq: str):
    prot_list = []
    for i in range(int(len(seq) / 3)):
        prot = rna_prot_map[seq[3 * i: 3 * i + 3]]
        if prot == 'Stop':
            break
        prot_list.append(prot)
    return ''.join(prot_list)


if __name__ == "__main__":
    in_path = "datasets/008.prot.in"
    out_path = "./datasets/008.prot.out"
    rna_seq = load_data(in_path)
    outstr = list_2_str(rna_2_protein(rna_seq), sep='')
    print(outstr)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(outstr + '\n')
    print(f"Save Result to {out_path}.")
