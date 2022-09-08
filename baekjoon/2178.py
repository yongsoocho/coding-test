from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().strip().split())

miro = [[0] * M for _ in range(N)]


for i in range(N):
    for j, val in enumerate(stdin.readline().strip()):
        miro[i][j] = int(val)

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)


def is_coordi_valid(x, y):
    return 0 <= y < N and 0 <= x < M


def bfs():
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    dq = deque()
    dq.append((0, 0, 1))

    while dq:
        x, y, d = dq.popleft()

        if y == N - 1 and x == M - 1:
            return d

        nd = d + 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if is_coordi_valid(nx, ny) and miro[ny][nx] == 1 and not visited[ny][nx]:
                dq.append((nx, ny, nd))
                visited[ny][nx] = True


print(bfs())
