# https://rosalind.info/problems/ba10d/
# Compute the Probability of a String Emitted by an HMM
# Script 004.ba10d.py created by minerw at 2022/09/05

# 给出outcome\transition\emission
# hidden path未知
# 求这个outcome的probability


# HMM(Σ, States, Transition, Emission)
def load_data(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as f:
        outcome = f.readline().strip()  # outcome
        f.readline()
        sigmas = f.readline().strip().split()  # sigmas
        f.readline()
        states = f.readline().strip().split()  # states
        f.readline()
        f.readline()
        transition = {}  # transition matrix
        for state in states:
            temp = f.readline().strip().split()
            transition[state] = {states[i]: float(temp[i + 1]) for i in range(len(states))}
        f.readline()
        f.readline()
        emission = {}  # emission matrix
        for state in states:
            temp = f.readline().strip().split()
            emission[state] = {sigmas[i]: float(temp[i + 1]) for i in range(len(sigmas))}
    return outcome, sigmas, states, transition, emission


def outcome_pr(outcome: str, states: list, transition: dict, emission: dict):
    # 用于存储概率信息的矩阵
    pr_dp = [[0 for _ in range(len(outcome))] for _ in range(len(states))]
    # 初始化概率矩阵
    for i in range(len(states)):
        pr_dp[i][0] = (1.0 / len(states)) * emission[states[i]][outcome[0]]
    # 逐个计算概率
    for i in range(1, len(outcome)):
        for j in range(len(states)):
            for k in range(len(states)):
                pr_dp[j][i] += pr_dp[k][i - 1] * transition[states[k]][states[j]] * emission[states[j]][outcome[i]]
    # 求和
    sum_pr = 0
    for i in range(len(states)):
        sum_pr += pr_dp[i][-1]
    return sum_pr


if __name__ == "__main__":
    inpath = "./datasets/004.ba10d.in"
    otc, sgs, sts, trans, emis = load_data(inpath)
    print(outcome_pr(otc, sts, trans, emis))
