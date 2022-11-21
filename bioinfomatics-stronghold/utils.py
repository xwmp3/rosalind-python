from data import load_rna_codon_table


def timer(func):
    def func_wrapper(*args, **kwargs):
        from time import time
        time_start = time()
        result = func(*args, **kwargs)
        time_end = time()
        print('{0} cost time {1} s'.format(func.__name__, time_end - time_start))

        return result

    return func_wrapper


def hamming_distance(s1: str, s2: str):
    if len(s1) != len(s2):
        raise ValueError("Not the same length!")

    return sum(es1 != es2 for es1, es2 in zip(s1, s2))


def count_nucleotides(seq: str, nmap: str = "ACGT") -> list:
    counts = [0 for _ in range(len(nmap))]
    for n in seq:
        counts[nmap.index(n)] += 1

    return counts


def dna_2_rna(seq: str) -> str:
    return ''.join([n if n != 'T' else 'U' for n in seq])


def rna_2_protein(seq: str) -> list:
    rna_prot_map = load_rna_codon_table()
    prot_list = []
    for i in range(int(len(seq) / 3)):
        prot = rna_prot_map[seq[3 * i: 3 * i + 3]]
        if prot == 'Stop':
            break
        prot_list.append(prot)
    return prot_list


def reverse_complement(seq: str, t: str = 'DNA') -> str:
    comp_dict = {}
    if t == 'DNA' or 'dna':
        comp_dict = {
            'A': 'T',
            'T': 'A',
            'C': 'G',
            'G': 'C'
        }
    elif t == 'RNA' or 'rna':
        comp_dict = {
            'A': 'U',
            'U': 'A',
            'C': 'G',
            'G': 'C'
        }
    else:
        print(f'Wrong type {t} for sequence to complement')
        exit(1)

    seq = seq.upper()  # dict is for upper case
    reverse_seq = seq[::-1]
    res = [comp_dict[n] for n in reverse_seq]

    return list_2_str(res, sep='')


def motif_prob(s: str, gc_content: float):
    gc_prob, at_prob = gc_content / 2, (1 - gc_content) / 2
    prob = 1
    for n in s:
        if n == 'A' or n == 'T':
            prob *= at_prob
        elif n == 'C' or n == 'G':
            prob *= gc_prob

    return prob


def list_2_str(x: list, sep: str = ' '):
    return sep.join([str(item) for item in x])
