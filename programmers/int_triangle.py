def solution(ta):
    table = [[0] * len(ta) for _ in range(len(ta))]
    table[0][0] = ta[0][0]

    for i in range(1, len(ta)):
        for j in range(len(ta[i])):
            if j == 0:
                table[i][j] = table[i - 1][j] + ta[i][j]
            elif j == len(ta[i]) - 1:
                table[i][j] = table[i - 1][j - 1] + ta[i][j]
            else:
                table[i][j] = max(table[i - 1][j - 1], table[i - 1][j]) + ta[i][j]

    return max(table[-1])
