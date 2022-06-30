import numpy as np

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

def gc_content(seq: str):
    count = 0
    for n in seq:
        if n == 'G' or n == 'C': 
            count += 1
    return count / len(seq)
    
if __name__ == "__main__":
    path = './datasets/05.gc.txt'
    names, seqs = load_fasta(path)
    print(seqs)
    gc_content_list = [gc_content(seq) * 100 for seq in seqs]
    highest_index = np.argmax(gc_content_list)
    print(f"{names[highest_index]}\n{gc_content_list[highest_index]}")