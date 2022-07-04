# https://rosalind.info/problems/hamm/

def hamming_distance(s1: str, s2: str):
    if len(s1) != len(s2):
        raise ValueError("Not the same length!")
    return sum(es1 != es2 for es1, es2 in zip(s1, s2))
    
if __name__ == "__main__":
    path = './datasets/006.hamm.txt'
    s1, s2 = "", ""
    with open(path, 'r') as f:
        s1 = f.readline().replace('\n', '').strip()
        s2 = f.readline().replace('\n', '').strip()
    print(s1, s2)
    print(hamming_distance(s1, s2))