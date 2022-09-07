def list_2_str(x: list, sep: str = ' '):
    return sep.join([str(item) for item in x])


def hidden_path_pr(start_pr: dict, path: str, transition: dict):
    pr = start_pr[path[0]]  # the initial probabilities are 'equal'
    for i in range(0, len(path) - 1):
        pr *= transition[path[i]][path[i+1]]
    return pr


def outcome_pr(emission: dict, outcome: str, hidden_path: str, init_pr=1):
    pr = init_pr
    for i in range(len(outcome)):
        pr *= emission[hidden_path[i]][outcome[i]]
    return pr