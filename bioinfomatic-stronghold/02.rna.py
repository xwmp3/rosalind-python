# https://rosalind.info/problems/rna/

def dna_2_rna(seq: str):
    return ''.join([n if n != 'T' else 'U' for n in seq])    

if __name__ == "__main__":
    path = "./datasets/02.rna.txt"
    data = ""
    with open(path, 'r') as f:
        data = f.readline().replace('\n', '')
    
    print(dna_2_rna(data))