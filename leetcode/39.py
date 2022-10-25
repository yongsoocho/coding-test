candidates, target = [2, 3, 6, 7], 7
ans = []


def dfs(goal, path):
    path.sort()

    if sum(path) == target and path not in ans:
        ans.append(path)
        return

    if sum(path) > target:
        return

    for i in range(len(candidates)):
        dfs(goal - candidates[i], path + [candidates[i]])


dfs(target, [])
print(ans)
