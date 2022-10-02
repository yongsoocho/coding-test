from collections import deque
import heapq

dq = deque()
hq = []

# print(dq) deque([])

# type(dq) <class 'collections.deque'>

dq.append("right")
dq.appendleft("left")
dq.pop()
dq.popleft()
dq.extend(["rightArr"])
dq.extendleft(["leftArr"])

print(dq)

# print(type(hq)) <class 'list'>

heapq.heappush(hq, 5)
heapq.heappush(hq, 2)
heapq.heappush(hq, 6)
heapq.heappush(hq, 3)
heapq.heappush(hq, 4)
heapq.heappush(hq, 1)

# print(hq) [1, 3, 2, 5, 4, 6]

while len(hq):
    print(hq[0]) # top-node 1 -> 2 -> 3 -> 4 -> 5 -> 6
    heapq.heappop(hq)
