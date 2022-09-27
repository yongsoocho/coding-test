from sys import stdin
from collections import deque

def solution():
    dq = deque()

    for c in stdin.readline().strip().lower():
        if c.isalnum():
            dq.append(c)


    while dq:
        if len(dq) == 1:
            return True

        if dq.popleft() != dq.pop():
            return False
        
    return True

print(solution())