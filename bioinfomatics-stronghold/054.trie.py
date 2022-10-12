# https://rosalind.info/problems/trie/
# Introduction to Pattern Matching
# Script 054.trie.py created by minerw at 2022/09/20

from itertools import count

from utils import list_2_str


def load_data(filepath: str) -> list:
    with open(filepath, 'r', encoding='utf-8') as f:
        seqs = [line.strip() for line in f]
    return seqs


class Trie:
    def __init__(self):
        self.counter = count(start=1)  # 从1开始的自增计数器
        self.root = [next(self.counter), {}]

    def insert(self, seq):
        node = self.root
        for n in seq:
            if n not in node[1]:
                node[1][n] = [next(self.counter), {}]
            node = node[1][n]

    def output(self):
        def format_trie(node):
            for ch, next_ in node[1].items():
                res.append(f"{node[0]} {next_[0]} {ch}")
                format_trie(next_)
        res = []
        format_trie(self.root)

        return res


def create_trie(seqs: list):
    trie = Trie()
    for s in seqs:
        trie.insert(s)
    return trie


if __name__ == "__main__":
    inpath = "./datasets/054.trie.in"
    outpath = "./datasets/054.trie.out"

    s_list = load_data(inpath)
    t = create_trie(s_list)
    outstr = list_2_str(t.output(), sep='\n')
    print(outstr)
    with open(outpath, 'w', encoding='utf-8') as out:
        out.write(outstr)
