n, k = 4, 2
nums = list(range(1, n + 1))
ans = []


def dfs(idx, path):
    if len(path) == k:
        ans.append(path)
        return

    if idx == n - 1:
        return

    dfs(idx + 1, path)
    dfs(idx + 1, path + [nums[idx + 1]])


dfs(0, [nums[0]])
dfs(0, [])
print(ans)
