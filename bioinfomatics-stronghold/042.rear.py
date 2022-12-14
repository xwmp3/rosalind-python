# https://rosalind.info/problems/rear/
# Reversal Distance
# 翻转距离

from utils import list_2_str


def load_data(filepath: str) -> list:
    pair_list = []
    with open(filepath, 'r') as f:
        lines = [item.replace('\n', '').strip() for item in f.readlines()]
        # 三行数据为一组（最后一行为空行）
        for i in range(0, int(len(lines) / 3)):
            p1 = [int(item) for item in lines[3 * i].split()]
            p2 = [int(item) for item in lines[3 * i + 1].split()]
            pair_list.append((p1, p2))
    return pair_list


def break_point(p):
    """
    Returns a list of elements in the given permutation where a breakpoint occurs.
    """
    bp = []
    for i in range(1, len(p)):
        if abs(p[i] - p[i - 1]) > 1:
            bp.append(i)
    return bp


def reversal_dist(p1, p2):
    print(p1, p2)
    """
    Determine the minimum reversal distance for a pair of permutations by
    performing a greedy search.
    """
    if p1 == p2:
        return 0
    ''' 
    Prepend 0 and append len(permutation) + 1 to determine if endpoints are correct. 
    '''
    p_start = [0] + [p1.index(x) + 1 for x in p2] + [len(p1) + 1]
    print('-' * 50, '\n', p_start, ' <-- reverse\n', sep='')
    '''
    Set starting permutations as the best current permutation.
    '''
    perm_list = [p_start]
    bp_min = len(break_point(p_start))
    print(bp_min)
    ''' 
    The maximum required number of reversals to solve this is len(permutation) + 1, 
    so loop until we hit that mark, or solve the problem.
    '''
    count = 0  # round count
    while count < len(p_start) + 1:
        print('Round #%i' % int(count + 1))
        new_perms = []
        count += 1
        for perm in perm_list:
            bp = break_point(perm)
            print(bp)
            ''' Reverse each pair of breakpoints '''
            for i in range(len(bp)):
                for j in range(i + 1, len(bp)):
                    a, b = bp[i], bp[j]
                    if b - a > 1:
                        p_new = perm[:a] + list(reversed(perm[a:b])) + perm[b:]
                        print(p_new)
                        bp_new = len(break_point(p_new))
                        '''
                        Problem solved when no breakpoints remain. 
                        The reversal(s) with the least breakpoints is/are the best choice in this case, 
                        so we can throw out the others.
                        '''
                        if bp_new == 0:
                            print('breakpoints = %i' % bp_new)
                            # printRound(p_new, a, b)
                            return count
                        elif bp_new < bp_min:
                            print('breakpoints = %i' % bp_new)
                            # printRound(p_new, a, b)
                            bp_min = bp_new
                            new_perms = [p_new]
                        elif bp_new == bp_min:
                            # printRound(p_new, a, b)
                            new_perms.append(p_new)
        perm_list = new_perms


if __name__ == '__main__':
    inpath = './datasets/042.rear.in'
    pairs = load_data(inpath)
    print(list_2_str([min(reversal_dist(p1, p2), reversal_dist(p2, p1)) for (p1, p2) in pairs]))
