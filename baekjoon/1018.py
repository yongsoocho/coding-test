from sys import stdin

M, N = map(int, stdin.readline().strip().split())

chess = [stdin.readline().strip() for _ in range(M)]

ans = 64  # 최대로 하고 내린다, 최대는 최소로 하고 올린다


def fill(x, y, bw):
    global ans
    count = 0
    for k in range(8):
        for p in range(8):
            if (k + p) % 2:
                if chess[x + k][y + p] == bw:
                    count += 1
            else:
                if chess[x + k][y + p] != bw:
                    count += 1

    ans = min(ans, count)


for i in range(M - 7):
    for j in range(N - 7):
        fill(i, j, 'B')
        fill(i, j, 'W')


print(ans)