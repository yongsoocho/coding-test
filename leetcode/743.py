
times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
N, K = 4, 2
ans = 0
table = [[1000] * N for _ in range(N)]
visited = [False] * N

for t in times:
    table[t[0] - 1][t[1] - 1] = t[2]

for i in range(N):
    for j in range(N):
        if i == j:
            table[i][j] = 0

visited[K - 1] = True


def dijkstra(start):
    visited[start] = True

    for q in range(N):
        if table[K - 1][q] > table[K - 1][start] + table[start][q]:
            table[K - 1][q] = table[K - 1][start] + table[start][q]

        if not visited[p] and table[K - 1][p] != 1000:
            dijkstra(q)


for p in range(N):
    if not visited[p] and table[K - 1][p] != 1000:
        dijkstra(p)

print(max(table[K - 1]))
