arr = list(map(int, input().strip().split()))

arr.sort()

ans = 0

for v in range(0, len(arr) - 1, 2):
    v
    ans += arr[v]

print(ans)