nums = [1, 2, 3]
ans = []


def dfs(path):
    # 길이가 같으면 백트래킹
    if len(nums) == len(path):
        ans.append(path)
        return

    # 배열안에 없다면 추가
    for i in nums:
        if i not in path:
            dfs(path + [i])


dfs([])
print(ans)
