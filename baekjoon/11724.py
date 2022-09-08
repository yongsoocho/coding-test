from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)  # recursion 반복

N, M = map(int, stdin.readline().strip().split())

matrix = [[0] * (N + 1) for _ in range(N + 1)]

visit = [False] * (N + 1)
visit[0] = True

result = 0


for _ in range(M):
    src, dest = map(int, stdin.readline().strip().split())
    matrix[src][dest] = matrix[dest][src] = 1


# for m in matrix:
#     print(m)

# def dfs(start):
#     global matrix
#     for index, edge in enumerate(matrix[start]):
#         if edge:
#             visit[index] = True
#
#
# dfs(1)


def dfs(src):
    for dest in range(N + 1):
        if matrix[src][dest] and not visit[dest]:
            visit[dest] = True
            dfs(dest)


# 일부로 range로 순회하여 인덱스 순회를 함
for i in range(N + 1):
    if not visit[i]:
        result += 1
        visit[i] = True
        dfs(i)


print(result)
