# https://rosalind.info/problems/pmch/
from math import factorial

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


def perfect_match_num(seq: str) -> int:
    au_count, cg_count = 0, 0
    for n in seq:
        if n == 'A' or n == 'U':
            au_count += 1
        elif n == 'C' or n == 'G':
            cg_count += 1
    return factorial(au_count / 2) * factorial(cg_count / 2)
    
if __name__ == '__main__':
    path = "./datasets/026.pmch.txt"
    rna_seq = load_fasta(path)[1][0]
    print(rna_seq)
    print(perfect_match_num(rna_seq))