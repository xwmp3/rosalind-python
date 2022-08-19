# https://rosalind.info/problems/kmp/

# Speeding Up Motif Finding

from data import load_fasta


def load_data(filepath: str):
    return load_fasta(filepath)[1][0]


def failure_array(s: str) -> list:
    f_a = [0 for _ in s]  # init failure array
    k = 0
    for i in range(2, len(s)):
        while k > 0 and s[k] != s[i - 1]:  # reset k
            k = f_a[k - 1]
        if s[k] == s[i - 1]:  #
            k += 1
        f_a[i - 1] = k
    return f_a


if __name__ == '__main__':
    inpath = "./datasets/037.kmp.txt"
    outpath = "./datasets/037.kmp.out"

    seq = load_data(inpath)
    f_a = failure_array(seq)

    outdata = ' '.join([str(item) for item in f_a])
    with open(outpath, 'w') as f:
        f.write(outdata + '\n')
    print(f"Save Results to {outpath}.")
