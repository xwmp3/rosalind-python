# https://rosalind.info/problems/splc/

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

def load_data(filepath: str):
    seqs = load_fasta(filepath)[1]
    dna_seq, intron_seqs = seqs[0], seqs[1:]
    return dna_seq, intron_seqs

def get_exon_concatenated(dna: str, introns: list) -> str:
    for intron in introns:
        dna = dna.replace(intron, '')
    return dna

def dna2rna(seq: str):
    return ''.join([n if n != 'T' else 'U' for n in seq]) 

def load_rna_codon_table(filepath: str):
    rna_prot_map = {}
    with open(filepath, 'r') as f:
        for line in f.readlines():
            datas = line.replace('\n', '').strip().split()
            for i in range(4):
                rna_seq, prot = datas[2 * i], datas[2 * i + 1]
                rna_prot_map[rna_seq] = prot
    return rna_prot_map

def rna2prot(rna_prot_map: dict, seq: str):
    prot_list = []
    for i in range(int(len(seq) / 3)):
        prot = rna_prot_map[seq[3 * i: 3 * i + 3]]
        if prot == 'Stop': break
        prot_list.append(prot)
    return ''.join(prot_list)

if __name__ == '__main__':
    path = "./datasets/022.splc.txt"
    codon_map = load_rna_codon_table("./datasets/008.rna-codon-table.txt")
    dna, introns = load_data(path)
    print(dna)
    print(introns)
    exon_concat = get_exon_concatenated(dna, introns)
    rna = dna2rna(exon_concat)
    prot = rna2prot(codon_map, rna)
    print(prot)