from sys import stdin
from itertools import combinations

# lengths = [int(stdin.readline().strip()) for _ in range(9)]
lengths = []

for _ in range(9):
    lengths.append(int(stdin.readline().strip()))


for arr in combinations(lengths, 2):
    if sum(arr) == sum(lengths) - 100:
        result = sorted(x for x in lengths if x not in arr)
        for y in result:
            print(y)
        break
