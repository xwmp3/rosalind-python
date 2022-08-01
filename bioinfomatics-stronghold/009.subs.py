# https://rosalind.info/problems/subs/

def load_st(filepath: str):
    s, t = '', ''
    with open(filepath, 'r') as f:
        s = f.readline().replace('\n', '').strip()
        t = f.readline().replace('\n', '').strip()
    return s, t

# naive string matcher
def find_motif(s: str, t: str):
    pos_list = []
    for i in range(0, len(s) - len(t)):
        if s[i: i + len(t)] == t:
            print(f'start: {i}, end: {i + len(t)}')
            pos_list.append(i + 1)
    return pos_list

if __name__ == '__main__':
    path = './datasets/009.subs.txt'
    s, t = load_st(path)
    pos_list = find_motif(s, t)
    print(' '.join([str(pos) for pos in pos_list]))