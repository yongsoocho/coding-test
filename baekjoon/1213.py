from sys import stdin
from collections import Counter

ipt = stdin.readline().strip()

count = {}

for s in ipt:
    if s in count:
        count[s] += 1
    else:
        count[s] = 1

if sum(i % 2 for i in count.values()) > 1:
    print("I'm Sorry Hansoo")
else:
    left = ""
    mid = ""

    for k, v in sorted(count.items()):
        left += k * (v // 2)

    for k, v in count.items():
        if v % 2:
            mid = k
            break

    print(left + mid + left[::-1])

#
#
# def pldr():
#     global ans
#     global ipt
#     if len(ipt) % 2 == 0:
#
#         for k in count:
#             if count[k] % 2 == 1:
#                 return print("I'm Sorry Hansoo")
#             else:
#                 ans += k * (count[k] // 2)
#
#         return print(ans + ans[::-1])
#
#     else:
#
#         mid = ""
#
#         for k in count:
#             if count[k] % 2 == 1:
#                 mid = k
#                 ans += k * (count[k] // 2)
#             else:
#                 ans += k * (count[k] // 2)
#
#         return print(ans + mid + ans[::-1])
#
#
# pldr()
