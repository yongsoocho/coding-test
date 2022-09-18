from sys import stdin

N, P = map(int, stdin.readline().strip().split())

ans = 0

pointer = {i: [] for i in range(7)}

for _ in range(N):
    L, PP = map(int, stdin.readline().strip().split())

    while pointer[L] and pointer[L][-1] > PP:
        pointer[L].pop()
        ans += 1

    if pointer[L] and pointer[L][-1] == PP:
        continue

    pointer[L].append(PP)
    ans += 1

    # if not pointer[L]:
    #     pointer[L].append(PP)
    #     ans += 1
    # elif pointer[L][-1] < PP:
    #     pointer[L].append(PP)
    #     ans += 1
    # elif pointer[L][-1] > PP:
    #     while True:
    #         if not pointer[L] or pointer[L][-1] < PP:
    #             ans += 1
    #             pointer[L].append(PP)
    #             break
    #         elif pointer[L][-1] > PP:
    #             ans += 1
    #             pointer[L].pop()


print(ans)
