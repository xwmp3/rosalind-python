# https://rosalind.info/problems/revp/

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

def other_strand_dna(seq: str):
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

def palindromic_recognition_site(seq1: str):
    res: list = []
    seq2 = other_strand_dna(seq1)[::-1]
    for i in range(2, len(seq2) - 1):
        for j in range(2, 7):
            if i - j < 0 or i + j > len(seq2):break
            if seq1[i-j:i] == seq2[i:i+j][::-1] and seq2[i-j:i] == seq1[i:i+j][::-1]:
                res.append((i - j + 1, i + j - (i - j)))
    return res

if __name__ == '__main__':
    path = "./datasets/021.revp.txt"
    seq = load_fasta(path)[1][0]
    for pos, length in palindromic_recognition_site(seq):
        print(pos, length)