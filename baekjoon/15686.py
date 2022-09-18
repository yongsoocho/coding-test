# from sys import stdin
#
# N, M = map(int, stdin.readline().strip().split())
#
# houses = []
# chickens = []
#
# for r in range(N):
#     for c, val in enumerate(map(int, stdin.readline().strip().split())):
#         if val == 1:
#             houses.append((r + 1, c + 1))
#         elif val == 2:
#             chickens.append((r + 1, c + 1))
#
#
# ans = N * N * N
#
#
# for chicken in chickens:
#     tot = 0
#     for house in houses:
#         tot += abs(chicken[0] - house[0]) + abs(chicken[1] - house[1])
#     ans = min(ans, tot)
#
#
# print(ans)


from sys import stdin
from itertools import combinations, permutations

N, M = map(int, stdin.readline().strip().split())

houses = []
chickens = []

ans = N * N * N

for i in range(N):
    for j, v in enumerate(map(int, stdin.readline().strip().split())):
        if v == 1:
            houses.append((i, j))
        elif v == 2:
            chickens.append((i, j))


def get_dist(h, c):
    return abs(h[0] - c[0]) + abs(h[1] - c[1])


for combi in combinations(chickens, M):
    tot = 0
    for h in houses:
        tot += min(get_dist(h, c) for c in combi)

    ans = min(ans, tot)


# print(ans)

test1 = [1, 2, 3, 4]
print(list(combinations(combinations(test1, 2), 2)))
print()
print(list(combinations(test1, 2)))
# print(list(permutations(permutations(test1, 2), 3)))
