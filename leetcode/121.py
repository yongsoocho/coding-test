from sys import stdin, maxsize

prices = list(map(int, stdin.readline().strip().split()))

l, profit = maxsize, 0

if len(prices) == 1:
    print(0)

for i in range(len(prices) - 2):
    l = min(l, prices[i])
    profit = max(profit, prices[i] - l)
    
print(profit)