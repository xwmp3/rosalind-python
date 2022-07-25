# https://rosalind.info/problems/hamm/

from utils import hamming_distance
    
if __name__ == "__main__":
    path = './datasets/006.hamm.txt'
    s1, s2 = "", ""
    with open(path, 'r') as f:
        s1 = f.readline().replace('\n', '').strip()
        s2 = f.readline().replace('\n', '').strip()
    print(s1, s2)
    print(hamming_distance(s1, s2))