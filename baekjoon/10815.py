from bisect import bisect_left, bisect_right
from sys import stdin

N = int(stdin.readline().strip())

cards = sorted(list(map(int, stdin.readline().strip().split())))

M = int(stdin.readline().strip())

goals = map(int, stdin.readline().strip().split())

result = []


# def bs(key):
#     mini = 0
#     maxi = N
#     midi = N // 2
#
#     while mini <= maxi:
#         if cards[midi] == key:
#             return "1"
#         elif cards[midi] > key:
#             maxi = midi - 1
#         elif cards[midi] < key:
#             mini = midi + 1
#         midi = (mini + maxi) // 2
#     return "0"
#
#
# for g in goals:
#     result.append(bs(g))
#
#
# print(' '.join(result))
for g in goals:
    l = bisect_left(cards, g)
    r = bisect_right(cards, g)
    result.append("1" if r - l > 0 else "0")

print(' '.join(result))
