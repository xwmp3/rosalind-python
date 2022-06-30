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
    
if __name__ == "__main__":
    datapath = './datasets/03.revc.txt'
    data = ""
    with open(datapath, 'r') as f:
        data = f.readline().replace('\n', '')
    print(len(data))
    print(other_strand_dna(data))