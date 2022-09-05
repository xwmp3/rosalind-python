# https://rosalind.info/problems/ba10b/

# Compute the Probability of an Outcome Given a Hidden Path

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
        emission_dict = {}
        for _ in range(len(states)):
            temp = f.readline().strip().split()
            emission_dict[temp[0]] = {sigma[i]: float(temp[i + 1]) for i in range(len(sigma))}
    print(f"Emission: {emission_dict}")
    return emission_dict, outcome_str, hidden_path


def outcome_probability_of_hidden_path(emission_map: dict, outcome: str, hidden_path: str):
    pr = 1
    for i in range(len(outcome)):
        pr *= emission_map[hidden_path[i]][outcome[i]]
    return pr


if __name__ == "__main__":
    inpath = "./datasets/002.ba10b.in"
    emission, x, pi = load_data(inpath)
    print(outcome_probability_of_hidden_path(emission, x, pi))