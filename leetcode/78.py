nums = [1, 2, 3]
ans = []


def dfs(index, path):
    if index == len(nums) - 1:
        ans.append(path)
        return

    dfs(index + 1, path + [nums[index + 1]])
    dfs(index + 1, path)


dfs(0, [])
dfs(0, [nums[0]])
print(ans)
