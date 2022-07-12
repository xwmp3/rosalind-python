# https://rosalind.info/problems/orf/

def load_fasta(filepath: str):
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
    return name_list, seq_list

def dna_reverse_implement(seq: str):
    reverse_seq = seq[::-1]
    res = []
    for n in reverse_seq:
        if n == 'A':
            res.append('T')
        elif n == 'T':
            res.append('A')
        elif n == 'C':
            res.append('G')
        elif n == 'G':
            res.append('C')
    return ''.join(res)

def load_rna_codon_table(filepath: str):
    rna_prot_map = {}
    with open(filepath, 'r') as f:
        for line in f.readlines():
            datas = line.replace('\n', '').strip().split()
            for i in range(4):
                rna_seq, prot = datas[2 * i], datas[2 * i + 1]
                rna_prot_map[rna_seq] = prot
    return rna_prot_map

def dna_2_rna(seq: str) -> str:
    return ''.join([n if n != 'T' else 'U' for n in seq])  

def rna_2_prot(seq: str, codon_map: dict, start_codon: str='AUG') -> list:
    prot_set = set()
    for i in range(0, len(seq) - 3):
        if seq[i:i+3] == start_codon:
            orf_seq = seq[i:]
            animo_list = [codon_map[orf_seq[3*j: 3*j+3]] for j in range(int(len(orf_seq) / 3))]
            if 'Stop' in animo_list:
                prot_set.add(''.join(animo_list[:animo_list.index('Stop')]))
    return prot_set

if __name__ == '__main__':
    codon_table_path = "./datasets/008.rna-codon-table.txt"
    path = './datasets/018.orf.txt'
    data = load_fasta(path)[1][0]
    rna_codon_map = load_rna_codon_table(codon_table_path)
    seqs = [data, dna_reverse_implement(data)]
    prots = set()
    for seq in seqs:
        rna_seq = dna_2_rna(seq)
        print(rna_seq)
        for p in rna_2_prot(rna_seq, rna_codon_map):
            prots.add(p)
    print("\n".join(list(prots)))