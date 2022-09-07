# https://rosalind.info/problems/ba10a/
# Compute the Probability of a Hidden Path

from utils import hidden_path_pr


# HMM(Σ, States, Transition, Emission)
def load_data(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as f:
        path = f.readline().strip()  # hidden path
        f.readline()
        states = f.readline().strip().split()  # states
        f.readline()
        f.readline()
        transition = {}
        for state in states:
            temp = f.readline().strip().split()
            transition[state] = {states[i]: float(temp[i + 1]) for i in range(len(states))}
    return path, states, transition


if __name__ == '__main__':
    inpath = './datasets/001.ba10a.in'
    hpath, sts, trans = load_data(inpath)
    start_p = {'A': 0.5, 'B': 0.5}
    print(hpath, sts, trans)
    print(hidden_path_pr(start_p, hpath, trans))
