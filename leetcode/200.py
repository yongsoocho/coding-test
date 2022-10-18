dy = (1, 0, -1, 0)
dx = (0, 1, 0, -1)

N = int(input().strip())
island = [input().strip() for _ in range(N)]
M = len(island[0])
visited = [[False] * M for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = True if island[i][j] == '0' else False


def dfs(x, y):
    if 0 <= x < N and 0 <= y < M and not visited[x][y] and island[x][y] == '1':
        print(x, y, visited)
        visited[x][y] = True

        for c in range(4):
            dfs(x + dx[c], y + dy[c])


for x in range(N):
    for y in range(M):
        if not visited[x][y]:
            ans += 1
            dfs(x, y)


print(ans)


# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         dy = (1, 0, -1, 0)
#         dx = (0, 1, 0, -1)
#         N, M = len(grid), len(grid[0])
#
#         visited = [[False] * M for _ in range(N)]
#         ans = 0
#
#         for i in range(N):
#             for j in range(M):
#                 if grid[i][j] == "0":
#                     visited[i][j] = True
#
#         def dfs(x, y):
#             if 0 <= x < N and 0 <= y < M and not visited[x][y] and grid[x][y] == '1':
#                 visited[x][y] = True
#
#                 for c in range(4):
#                     dfs(x + dx[c], y + dy[c])
#
#         for x in range(N):
#             for y in range(M):
#                 if not visited[x][y]:
#                     ans += 1
#                     dfs(x, y)
#
#         return ans