N, L = map(int, input().strip().split())
need_fixed = list(map(int, input().strip().split()))
need_fixed.sort()
pointer = 0
ans = 0

for idx in need_fixed:
    if pointer < idx:
        ans += 1
        pointer = idx + L - 1

print(ans)