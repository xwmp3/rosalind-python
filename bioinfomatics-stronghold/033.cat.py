# https://rosalind.info/problems/cat/

def load_fasta(filepath: str):
    name_list, seq_list = [], []
    with open(filepath, 'r') as fasta:
        while True:
            line = fasta.readline()
            if not line:
                break
            data = line.replace('\n', '').strip()
            if data.startswith('>'):
                name_list.append(data[1:])
                line = fasta.readline().replace('\n', '').strip()
                seq_list.append(line)
            else:
                seq_list[len(seq_list) - 1] += line.replace('\n', '').strip()
    return name_list, seq_list

def load_data(filepath: str):
    return load_fasta(filepath)[1][0]

# https://github.com/cdeterman/Rosalind
def noncrossing_perfect_matches_recursive(seq: str, cache: dict):
    if seq not in cache:
        temp = []
        for k in range(1, len(seq), 2):
            '''
            Multiply first half of the string * the first nt and ending nt of first half
            * second half
            This multiplication is to combine the number of noncrossing
            perfect matches from the subproblems.
            The actual value/counts comes from the dynamically generated dictionary.
            '''
            temp.append(noncrossing_perfect_matches_recursive(seq[1:k], cache) * cache[seq[0] + seq[k]] * noncrossing_perfect_matches_recursive(seq[k+1:], cache))
        cache[seq] = sum(temp)
    return cache[seq]
    
    
if __name__ == '__main__':
    path = "./datasets/033.cat.txt"
    seq = load_data(path)
    modulo = 10 ** 6
    # print(seq)
    init_cache = {
        '': 1, 
        'A': 0, 'C': 0, 'G': 0, 'U': 0, 
        'AA': 0, 'AC': 0, 'AG': 0, 'AU': 1, 
        'CA': 0, 'CC': 0, 'CG': 1, 'CU': 0, 
        'GA': 0, 'GC': 1, 'GG': 0, 'GU': 0, 
        'UA': 1, 'UC': 0, 'UG': 0, 'UU': 0
    }
    print(noncrossing_perfect_matches_recursive(seq, init_cache) % modulo)