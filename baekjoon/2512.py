from sys import stdin

N = int(stdin.readline().strip())

requests = sorted(list(map(int, stdin.readline().strip().split())))

budget_limit = int(stdin.readline().strip())

pointer = (requests[0] + requests[-1]) // 2


# def request_sum(li):
#     rs = 0
#
#     for req in requests:
#         if req <= li:
#             rs += req
#         else:
#             rs += li
#
#     return rs
#
#
# if request_sum(avg) > budget_limit:
#     while request_sum(avg) > budget_limit:
#         avg -= 1
#
#     print(avg)
# elif request_sum(avg) < budget_limit:
#     print(requests[-1])

def isLimited(li):
    return sum(min(r, li) for r in requests) <= budget_limit
    # rs = 0
    #
    # for req in requests:
    #     if req <= li:
    #         rs += req
    #     else:
    #         rs += li
    #
    # return rs > budget_limit


lo = 0
hi = max(requests)
mid = (lo + hi) // 2
ans = 0

while lo <= hi:
    if isLimited(mid):
        lo = mid + 1
        ans = mid
    else:
        hi = mid - 1

    mid = (lo + hi) // 2

print(ans)