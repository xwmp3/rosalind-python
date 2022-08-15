# https://rosalind.info/problems/ba10a/

def load_data(filepath: str):
    f = open(filepath, 'r')
    path_string = f.readline().replace('\n', '').strip()
    prs_dict = {}
    f.readline()
    states = f.readline().replace('\n', '').strip().split()
    f.readline()
    f.readline()
    temp_prs = []
    for _ in range(2):
        temp_prs += [float(pr) for pr in f.readline().replace('\n', '').strip().split()[1:]]
    for i, name in enumerate(['AA', 'AB', 'BA', 'BB']):
        prs_dict[name] = temp_prs[i]
    f.close()
    return path_string, prs_dict


def path_pr(path_str: str, prs_dict: dict):
    pr = 0.5
    for i in range(0, len(path_str) - 1):
        key = path_str[i:i + 2]
        pr *= pr_dict[key]
    return pr


if __name__ == '__main__':
    path = './datasets/001.ba10a.txt'
    path_string, pr_dict = load_data(path)
    print(path_string, pr_dict)
    print(path_pr(path_string, pr_dict))
