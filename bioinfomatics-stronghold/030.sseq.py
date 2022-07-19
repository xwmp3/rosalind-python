# https://rosalind.info/problems/sseq/

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

def load_data(filepath: str) -> tuple:
    s, t = load_fasta(filepath)[1]
    return s, t

def subseq_pos(s: str, t: str):
    pos_list = [[i+1 for i, x in enumerate(s) if x == n] for n in t]
    sub_pos = [pos_list[0][0]]
    for pos in pos_list[1:]:
        for p in pos:
            if p > sub_pos[-1] + 1:
                sub_pos.append(p)
                break
    return sub_pos
    
if __name__ == '__main__':
    path = "./datasets/030.sseq.txt"
    s, t = load_data(path)
    print(' '.join([str(d) for d in subseq_pos(s, t)]))