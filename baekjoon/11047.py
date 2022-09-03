from sys import stdin

N, K = map(int, stdin.readline().strip().split())

coins = []
result = 0

for _ in range(N):
    coins.append(int(stdin.readline().strip()))

for coin in coins[::-1]:
    amount = K // coin
    result += amount
    K -= amount * coin

    if K == 0:
        break

print(result)