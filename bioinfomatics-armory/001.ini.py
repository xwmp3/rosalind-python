# https://rosalind.info/problems/ini/

# Introduction to the Bioinformatics Armory


def load_data(filepath: str) -> str:
    with open(filepath, 'r') as f:
        data = f.readline().replace('\n', '')
    return data


def count_nucleotides(seq: str, nmap: str = "ACGT"):
    counts = [0 for _ in range(len(nmap))]
    for n in seq:
        counts[nmap.index(n)] += 1
    return counts


if __name__ == "__main__":
    inpath = './datasets/001.ini.in'
    seq = load_data(inpath)
    print(f"Seq length: {len(seq)}")
    print(' '.join([str(count) for count in count_nucleotides(seq)]))
