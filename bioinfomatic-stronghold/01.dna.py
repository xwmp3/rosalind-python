# https://rosalind.info/problems/dna/

def count_nucleotides(seq: str, nmap: str="ACGT"):
    counts = [0 for _ in range(len(nmap))]
    for n in seq:
        counts[nmap.index(n)] += 1
    return counts
    
if __name__ == "__main__":
    datapath = './datasets/01.dna.txt'
    data = ""
    with open(datapath, 'r') as f:
        data = f.readline().replace('\n', '')
    print(len(data))
    print(count_nucleotides(data))