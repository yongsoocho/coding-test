from sys import stdin

N = int(stdin.readline().strip())

table = [[0] * (N + 1) for i in range(N + 1)]

ans = 0

R = N // 2

for k in range(N + 1):
    for n in range(k, N + 1):
        if k == 0:
            table[k][n] = 1
        elif k == 1:
            table[k][n] = n
        elif n == k:
            table[k][n] = 1
        else:
            table[k][n] = table[k-1][n-1] + table[k][n-1]


for r in range(R + 1):
    ans += table[r][N - r]


print(ans % 10007)
