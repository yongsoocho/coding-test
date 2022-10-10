from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)  # recursion 반복

N, M = map(int, stdin.readline().strip().split())

visited = [False] * N
Matrix = [[0] * N for _ in range(N)]
for _ in range(M):
    start, end = map(int, stdin.readline().strip().split())
    Matrix[start - 1][end - 1] = Matrix[end - 1][start - 1] = 1

ans = 0


def dfs(idx):
    for nxt in range(N):
        if Matrix[idx][nxt] == 1 and not visited[nxt]:
            visited[nxt] = True
            dfs(nxt)


for i in range(N):
    if not visited[i]:
        ans += 1
        visited[i] = True
        dfs(i)


print(ans)
