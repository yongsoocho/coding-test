digits = "23"
dic = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}
ans = []


def dfs(idx, path):
    if len(path) == len(digits):
        ans.append(path)
        return

    for c in dic[digits[idx]]:
        dfs(idx + 1, path + c)


dfs(0, "")
print(ans)
