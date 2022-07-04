# https://rosalind.info/problems/ini/

def count_nucleotides(seq: str, nmap: str="ACGT"):
    counts = [0 for _ in range(len(nmap))]
    for n in seq:
        counts[nmap.index(n)] += 1
    return counts
    
if __name__ == "__main__":
    datapath = './datasets/001.ini.txt'
    data = ""
    with open(datapath, 'r') as f:
        data = f.readline().replace('\n', '')
    print(f"Seq length: {len(data)}")
    print(' '.join([str(count) for count in count_nucleotides(data)]))