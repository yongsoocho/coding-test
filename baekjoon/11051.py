from sys import stdin

N, K = map(int, stdin.readline().strip().split())

table = [[0] * (N + 1) for i in range(N + 1)]

for k in range(N + 1):
    for n in range(N + 1): # range(k, N + 1) 로 하자!
        if k == 0:
            table[k][n] = 1
        elif k == 1 and n >= 1:
            table[k][n] = n
        elif n >= k:
            table[k][n] = table[k-1][n-1] + table[k][n-1]


print(table[K][N] % 10007)
