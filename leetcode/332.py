tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
tickets.sort()
ans = []
N = len(tickets)


def dfs(arg):
    global ans

    if len(arg) == N + 1:
        ans = arg[:]
        return

    last = arg.pop()

    for idx in range(len(tickets)):
        if tickets[idx][0] == last:
            t0, t1 = tickets.pop(idx)
            dfs(arg + [t0] + [t1])
            break # 이것 때문에 에러 떳음


for idx in range(N):
    if tickets[idx][0] == "JFK":
        t0, t1 = tickets.pop(idx)
        dfs([] + [t0] + [t1])
        break


print(ans)
