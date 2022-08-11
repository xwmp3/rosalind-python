# https://rosalind.info/problems/motz/

# Motzkin Numbers and RNA Secondary Structures

from data import load_fasta

def load_data(filepath: str) -> str:
    return load_fasta(filepath)[1][0]

'''
Returns the number of noncrossing bonding graphs for a given RNA sequence.
'''
def noncrossing_matches_recursive(seq: str, cache: dict) -> int:
    matchings = {'A':'U', 'U':'A', 'C':'G', 'G':'C'}    
    # Only one possible way to match if the length is at most one.
    if len(seq) <= 1: 
        return 1
    else:
        if seq in cache: # If we've already computed the value, return it!
            return cache[seq]
        else: # Otherwise, calculate the value, add it to the dictionary, and return it.
            subintervals = []
            for i in range(1, len(seq)):
                if seq[0] == matchings[seq[i]]:
                    subintervals.append([seq[1:i], seq[i + 1:]])
            # Reduce the problem to noncrossing matchings over the matching substrings, and the matchings for the next starting point.
            cache[seq] = sum(
                [noncrossing_matches_recursive(subint[0], cache) * noncrossing_matches_recursive(subint[1], cache) 
                 for subint in subintervals]
            ) + noncrossing_matches_recursive(seq[1:], cache)
            return cache[seq]

if __name__ == '__main__':
    inpath = "./datasets/048.motz.txt"
    module = 10 ** 6
    seq = load_data(inpath)
    print(seq)
    init_cache = {}
    print(noncrossing_matches_recursive(seq, init_cache) % module)
