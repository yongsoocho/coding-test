import heapq
from sys import stdin

hq = []

for _ in range(int(stdin.readline().strip())):

    x = int(stdin.readline().strip())

    if x == 0:
        print(heapq.heappop(hq)[1] if len(hq) != 0 else 0)
    else:
        heapq.heappush(hq, (abs(x), x))  # (절댓값, 원본값) -> 절댓값이 제일 낮은 얘를 먼저 뽑고, 같은 것 중에는 원본값이 제일 낮은 것을 뽑
