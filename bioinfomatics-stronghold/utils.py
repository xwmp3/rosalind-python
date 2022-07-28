def timer(func):
    def func_wrapper(*args,**kwargs):
        from time import time
        time_start = time()
        result = func(*args,**kwargs)
        time_end = time()
        print('{0} cost time {1} s'.format(func.__name__, time_end - time_start))
        return result
    return func_wrapper

def hamming_distance(s1: str, s2: str):
    if len(s1) != len(s2):
        raise ValueError("Not the same length!")
    return sum(es1 != es2 for es1, es2 in zip(s1, s2))

def load_fasta(filepath: str) -> (list, list):
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

def count_nucleotides(seq: str, nmap: str="ACGT") -> list:
    counts = [0 for _ in range(len(nmap))]
    for n in seq:
        counts[nmap.index(n)] += 1
    return counts

def dna_2_rna(seq: str) -> str:
    return ''.join([n if n != 'T' else 'U' for n in seq])

def dna_reverse_implement(seq: str) -> str:
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

def load_rna_codon_table(
    filepath: str="./datasets/008.rna-codon-table.txt") -> dict:
    rna_prot_map = {}
    with open(filepath, 'r') as f:
        for line in f.readlines():
            datas = line.replace('\n', '').strip().split()
            for i in range(4):
                rna_seq, prot = datas[2 * i], datas[2 * i + 1]
                rna_prot_map[rna_seq] = prot
    return rna_prot_map

def load_prot_mass_table(
    filepath: str="./datasets/020.monoisotopic-mass-table.txt") -> dict:
    mass_dict = {}
    with open(filepath, 'r') as f:
        for line in f.readlines():
            data = line.replace('\n', '').strip().split()
            mass_dict[data[0]] = float(data[1])
    return mass_dict