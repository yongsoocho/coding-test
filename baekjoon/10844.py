from sys import stdin

N = int(stdin.readline().strip())

ans = 0

"""
f(n: 길이, d: 마지막 숫자) = f(n - 1, d - 1) + f(n - 1, d + 1)
다음과 같은 점화식을 세우기 위해서는 '영향을 주는 것을 찾아라!(d: 마지막 숫자)'
"""

table = [[0] * 10 for _ in range(N + 1)]

for i in range(10):
    table[1][i] = 1 if  i else 0

for i in range(2, N + 1):
    for j in range(10):
        if j == 0:
            table[i][j] = table[i-1][j+1]
        elif j == 9:
            table[i][j] = table[i-1][j-1]
        else:
            table[i][j] = table[i-1][j-1] + table[i-1][j+1]


# for p in table:
#     print(p)


for v in table[N]:
    ans += v


print(ans % 1000000000)
