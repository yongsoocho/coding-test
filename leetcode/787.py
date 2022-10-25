from collections import defaultdict
import heapq

n, src, dst, k = 3, 0, 2, 0
edges = [
    [0, 1, 100],
    [1, 2, 100],
    [0, 2, 500]
]

graph = defaultdict(list)

for s, e, w in edges:
    graph[s].append((e, w))


Q = [(0, src)]
dict = defaultdict(int)

while Q:
    time, node = heapq.heappop()

