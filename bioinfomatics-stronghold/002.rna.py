# https://rosalind.info/problems/rna/

from utils import dna_2_rna    

if __name__ == "__main__":
    path = "./datasets/002.rna.txt"
    data = ""
    with open(path, 'r') as f:
        data = f.readline().replace('\n', '')
    
    print(dna_2_rna(data))