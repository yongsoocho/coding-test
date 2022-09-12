from sys import stdin

N = int(stdin.readline().strip())

pibo = [0, 1, 1]

for i in range(N):
    if i >= 3:
        pibo.append(pibo[i - 1] + pibo[i - 2])

print(pibo[N - 1] + pibo[N - 2])
