nums = list(map(int, input().strip().split()))

p = 1
ans = []

for i in range(len(nums)):
    ans.append(p)
    p *= nums[i]
    
    
p = 1
for i in range(len(nums) - 1, -1, -1):
    print(i)
    
    ans[i] = ans[i] * p
    p = p * nums[i]
    
print(ans)