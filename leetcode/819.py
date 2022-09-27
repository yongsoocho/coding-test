## 정규식으로 풀어야함 ##

paragraph = input().strip().lower().split(",")
banned = input().lower()

table = {}

for p in paragraph:
    word = p if p[-1].isalpha() else p[:-1]
    
    if word in table:
        table[word] += 1
    else:
        table[word] = 1
        
ans = sorted(table.items(), key=lambda x: (-x[1], x[0]))
print(ans)
print(ans[0][0] if ans[0][0] != banned else ans[1][0])