# https://rosalind.info/problems/scsp/

# Interleaving Two Motifs

# 求两个序列的最短共同超序列
# 字符串、动态规划、状态方程、递归

def load_data(filepath: str) -> tuple:
    with open(filepath, 'r', encoding='utf-8') as f:
        s1 = f.readline().replace('\n', '').strip()
        s2 = f.readline().replace('\n', '').strip()

    return s1, s2


# https://www.geeksforgeeks.org/print-shortest-common-supersequence/
# https://www.geeksforgeeks.org/shortest-common-supersequence/

# A dynamic programming based Python3 program print shortest supersequence of two strings
# returns shortest supersequence of X and Y
def printShortestSuperSeq(m, n, x, y):
    # dp[i][j] contains length of shortest
    # supersequence for X[0..i-1] and Y[0..j-1]
    dp = [[0 for i in range(n + 1)]
          for j in range(m + 1)]

    # Fill table in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):
            # Below steps follow recurrence relation
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif x[i - 1] == y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],
                                   dp[i][j - 1])

    # Following code is used to print
    # shortest supersequence

    # dp[m][n] stores the length of the
    # shortest supersequence of X and Y

    # string to store the shortest supersequence
    string = ""

    # Start from the bottom right corner and
    # add the characters to the output string
    i = m
    j = n
    while i * j > 0:
        # If current character in X and Y are same,
        # then current character is part of
        # shortest supersequence
        if x[i - 1] == y[j - 1]:
            # Put current character in result
            string = x[i - 1] + string
            # reduce values of i, j and index
            i -= 1
            j -= 1

        # If current character in X and Y are different
        elif dp[i - 1][j] > dp[i][j - 1]:
            # Put current character of Y in result
            string = y[j - 1] + string
            # reduce values of j and index
            j -= 1
        else:
            # Put current character of X in result
            string = x[i - 1] + string
            # reduce values of i and index
            i -= 1

    # If Y reaches its end, put remaining characters
    # of X in the result string
    while i > 0:
        string = x[i - 1] + string
        i -= 1

    # If X reaches its end, put remaining characters
    # of Y in the result string
    while j > 0:
        string = y[j - 1] + string
        j -= 1

    return string


if __name__ == "__main__":
    inpath = "./datasets/050.scsp.txt"
    motif1, motif2 = load_data(inpath)
    print(motif1, motif2)

    m, n = len(motif1), len(motif2)
    # Take the smaller string as x and larger one as y
    if m > n:
        motif1, motif2 = motif2, motif1
        m, n = len(motif1), len(motif2)

    print(printShortestSuperSeq(m, n, motif1, motif2))

