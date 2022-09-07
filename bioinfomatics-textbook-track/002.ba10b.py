# https://rosalind.info/problems/ba10b/

# Compute the Probability of an Outcome Given a Hidden Path

from utils import outcome_pr


# HMM(Σ, States, Transition, Emission)
# Pr(x|pi)
# x -> outcome string
# pi -> hidden path
def load_data(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as f:
        outcome_str = f.readline().strip()
        f.readline()  # 跳过分割线
        sigma = f.readline().strip().split()
        f.readline()
        hidden_path = f.readline().strip()
        f.readline()
        states = f.readline().strip().split()
        f.readline()
        f.readline()
        emission = {}
        for _ in range(len(states)):
            temp = f.readline().strip().split()
            emission[temp[0]] = {sigma[i]: float(temp[i + 1]) for i in range(len(sigma))}
    return emission, outcome_str, hidden_path


if __name__ == "__main__":
    inpath = "./datasets/002.ba10b.in"
    emis, x, pi = load_data(inpath)
    print(outcome_pr(emis, x, pi))
