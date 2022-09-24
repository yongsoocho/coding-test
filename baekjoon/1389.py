from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().strip().split())

table = [[] for _ in range(N)]

# 1. table 채워 넣기
for _ in range(N):
    x, y = map(int, stdin.readline().strip().split())
    table[x - 1].append(y - 1)
    table[y - 1].append(x - 1)

kevin = [0] * N  # 케빈 값 저장
ans = (-1, N * N)  # (인덱스, 값)


# start 에서 goal 까지 넓이 우선 탐색
def bfs(start, goal):
    visited = [False] * N
    visited[start] = True
    dq = deque()
    dq.append((start, 0))
    while dq:
        now, d = dq.popleft()
        if now == goal:
            return d
        nd = d + 1
        for nxt in table[now]:
            if not visited[nxt]:
                visited[nxt] = True
                dq.append((nxt, nd))


# 4. start 의 케빈 베이컨 값 구하기
# start 에서 j 까지의 bfs 구해서 더하기
def get_kevin(start):
    tot = 0

    for j in range(N):
        if j != start:
            tot += bfs(start, j)

    return tot


# 3. kevin table 에 값 채우기
for i in range(N):
    kevin[i] = get_kevin(i)


# 2. kevin table 을 보고 ans 에 값넣기
for i in range(N):
    if ans[1] > kevin[i]:
        ans = (i, kevin[i])


print(ans[0] + 1)
