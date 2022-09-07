# https://rosalind.info/problems/ba10c/
# Implement the Viterbi Algorithm
# Script 003.ba10c.py created by minerw at 2022/09/05

# 维特比算法（动态规划）
# 用于计算HMM中Pr(x,pi)最大时的隐藏状态序列（维特比路径）

from utils import list_2_str


# HMM(Σ, States, Transition, Emission)
def load_data(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as f:
        outcome = f.readline().strip()
        f.readline()  # delimiter
        sigmas = f.readline().strip().split()
        f.readline()  # delimiter
        states = f.readline().strip().split()
        f.readline()  # delimiter
        f.readline()  # header of transition
        # load transtion matrix
        transition = {}
        for state in states:
            temp = f.readline().strip().split()
            transition[state] = {states[i]: float(temp[i + 1]) for i in range(len(states))}
        f.readline()  # delimiter
        f.readline()  # header of emission
        # load emission matrix
        emission = {}
        for state in states:
            temp = f.readline().strip().split()
            emission[state] = {sigmas[i]: float(temp[i + 1]) for i in range(len(sigmas))}
    return outcome, sigmas, states, transition, emission


# https://en.wikipedia.org/wiki/Viterbi_algorithm#Example
def viterbi(outcome, states, transmition, emission):
    dp = [{}]
    for st in states:
        dp[0][st] = {
            "prob": 1 * emission[st][outcome[0]],
            "prev": None
        }
    # Run Viterbi when t > 0
    for t in range(1, len(outcome)):
        dp.append({})
        for st in states:
            max_tr_prob = dp[t - 1][states[0]]["prob"] * transmition[states[0]][st]
            preb_st_selected = states[0]
            for prev_st in states[-1:]:
                tr_prob = dp[t - 1][prev_st]["prob"] * transmition[prev_st][st]
                if tr_prob > max_tr_prob:
                    max_tr_prob = tr_prob
                    preb_st_selected = prev_st
            max_prob = max_tr_prob * emission[st][outcome[t]]
            dp[t][st] = {
                "prob": max_prob,
                "prev": preb_st_selected
            }

    #print dp
    for line in show_dptable(dp): print(line)

    opt = []
    max_prob = 0.0
    best_st = None
    # Get the most probable state and its backtrack
    for st, data in dp[-1].items():
        if data["prob"] > max_prob:
            max_prob = data["prob"]
            best_st = st
    opt.append(best_st)
    previous = best_st

    # Follow the backtracks till the first outcome
    for t in range(len(dp) - 2, -1, -1):
        opt.insert(0, dp[t + 1][previous]["prev"])
        previous = dp[t + 1][previous]["prev"]

    print("The steps of states are " + list_2_str(opt, sep='')
          + " with highest probability of %s" % max_prob)
    return list_2_str(opt, sep='')


def show_dptable(dp_table):
    # Print a table of steps from dictionary
    yield " " * 5 + "     ".join(("%3d" % i) for i in range(len(dp_table)))
    for state in dp_table[0]:
        yield "%.7s: " % state + " ".join("%.7s" % ("%lf" % v[state]["prob"]) for v in dp_table)


if __name__ == "__main__":
    inpath = "./datasets/003.ba10c.in"
    otc, _, sts, trans, emis = load_data(inpath)
    print(viterbi(outcome=otc, states=sts, transmition=trans, emission=emis))
