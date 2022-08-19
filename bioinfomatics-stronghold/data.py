def load_fasta(filepath: str, is_dict: bool = False):
    name_list, seq_list = [], []
    with open(filepath, 'r') as fasta:
        while True:
            line = fasta.readline()
            if not line:
                break
            data = line.replace('\n', '').strip()
            if data.startswith('>'):
                name_list.append(data[1:])
                line = fasta.readline().replace('\n', '').strip()
                seq_list.append(line)
            else:
                seq_list[len(seq_list) - 1] += line.replace('\n', '').strip()
    print(f"Load {len(seq_list)} fasta seqs from {filepath}")
    if is_dict:
        fasta_dict = {}
        name_list, seq_list = load_fasta(filepath)
        for i, name in enumerate(name_list):
            fasta_dict[name] = seq_list[i]
        return fasta_dict
    else:
        return name_list, seq_list


def load_rna_codon_table(
        filepath: str = "./datasets/008.rna-codon-table.txt") -> dict:
    rna_prot_map = {}
    with open(filepath, 'r') as f:
        for line in f.readlines():
            datas = line.replace('\n', '').strip().split()
            for i in range(4):
                rna_seq, prot = datas[2 * i], datas[2 * i + 1]
                rna_prot_map[rna_seq] = prot
    return rna_prot_map


def load_prot_mass_table(
        filepath: str = "./datasets/020.monoisotopic-mass-table.txt") -> dict:
    mass_dict = {}
    with open(filepath, 'r') as f:
        for line in f.readlines():
            data = line.replace('\n', '').strip().split()
            mass_dict[data[0]] = float(data[1])
    return mass_dict
