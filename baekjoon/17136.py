from sys import stdin

table = [list(map(int, stdin.readline().strip().split())) for _ in range(10)]

papers = [0] * 6

ans = 25


def is_possible(y, x, sz):
    if papers[sz] == 5:
        return False

    if y + sz > 10 or x + sz > 10:
        return False

    for i in range(sz):
        for j in range(sz):
            if table[y + i][x + j] == 0:
                return False

    return True


def mark(y, x, sz, v):
    for i in range(sz):
        for j in range(sz):
            table[y + i][x + j] = v

    if v:
        papers[sz] -= 1
    else:
        papers[sz] += 1


def backtracking(y, x):
    global ans
    if y == 10:
        ans = min(ans, sum(papers))
        return

    if x == 10:
        backtracking(y + 1, 0)
        return

    if table[y][x] == 0:
        backtracking(y, x + 1)
        return

    for sz in range(1, 6):
        if is_possible(y, x, sz):
            mark(y, x, sz, 0)
            backtracking(y, x + 1)
            mark(y, x, sz, 1)  # 원상복구


backtracking(0, 0)
print(-1 if ans == 25 else ans)
