# https://rosalind.info/problems/dna/

from utils import count_nucleotides
    
if __name__ == "__main__":
    datapath = './datasets/001.dna.txt'
    data = ""
    with open(datapath, 'r') as f:
        data = f.readline().replace('\n', '')
    print(len(data))
    print(' '.join([str(count) for count in count_nucleotides(data)]))