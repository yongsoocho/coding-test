"""
1. 맨 앞 값을 삭제 (독해)
2. 맨 앞의 값을 뒤로 추가 (독해)
3. 배열은 추가/삭제 시간복잡도가 O(n)
4. 추가/삭제 가 O(1)인 Queue를 이용하자!!
"""


# from sys import stdin
#
# cards = list(map(lambda x: x + 1, range(int(stdin.readline().strip()))))
#
# for idx, val in enumerate(cards):
#     if (idx + 1) % 2 == 1 and len(cards) > 1:
#         if idx + 1 <= len(cards):
#             cards.append(cards[idx + 1])
#         cards.pop(idx)
#         cards.pop(idx)
#
#     if len(cards) == 1:
#         break
#
# print(cards[0])

from sys import stdin
from collections import deque

N = int(stdin.readline().strip())
dq = deque(range(1, N + 1)) # N까지 하면 N-1까지 반복이 되기 때문에 조심하자!

while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq[0])



