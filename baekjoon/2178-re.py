from collections import deque
N, M = map(int, input().strip().split())

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

Matrix = [""] * N
visited = [[False] * M for _ in range(N)]
for i in range(N):
    Matrix[i] = input().strip()


dq = deque()
dq.append((0, 0, 1))
visited[0][0] = True
ans = 0


def valid(x, y):
    if 0 <= x < N and 0 <= y < M and Matrix[x][y] == "1" and not visited[x][y]:
        return True

    return False


while dq:
    now_x, now_y, ans = dq.popleft()
    if now_x == N - 1 and now_y == M - 1:
        break

    for co in range(4):
        nxt_x = int(now_x + dx[co])
        nxt_y = int(now_y + dy[co])
        if valid(nxt_x, nxt_y):
            visited[nxt_x][nxt_y] = True
            dq.append((nxt_x, nxt_y, ans + 1))


print(ans)
