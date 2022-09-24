from sys import stdin

N, M = map(int, stdin.readline().strip().split())

table = [stdin.readline().strip() for _ in range(N)]
dp = [[0] * M for _ in range(N)]

ans = 0

for t in range(M):
    if table[0][t] == '1':
        dp[0][t] = 1


for i in range(1, N):
    if table[i][0] == '1':
        dp[i][0] = 1

    for j in range(1, M):
        if table[i][j] == '1':
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1  # dp는 점화식으로 푼다


for i in range(N):
    for j in range(M):
        ans = max(ans, dp[i][j])


print(ans ** 2)

#
# for i in range(N):
#     table[i] = stdin.readline().strip()
#
#
# def square_check(x, y):
#     size = 1
#
#     k = 1
#     for xv in range(k):
#         for yv in range(k):
#
#
#     return size
#
#
# for i in range(N):
#     for j in range(M):
#         if table[i][j] == '1':
#             ans = max(ans, square_check(i, j))