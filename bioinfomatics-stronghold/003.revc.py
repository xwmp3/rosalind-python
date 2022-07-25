# https://rosalind.info/problems/revc/

from utils import dna_reverse_implement
    
if __name__ == "__main__":
    datapath = './datasets/003.revc.txt'
    data = ""
    with open(datapath, 'r') as f:
        data = f.readline().replace('\n', '')
    print(len(data))
    print(dna_reverse_implement(data))