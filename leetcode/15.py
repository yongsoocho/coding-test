nums = list(map(int, list(input().strip().split())))

nums.sort()
ans = []

for p in range(1, len(nums) - 1):
    
    i, j = 1, 1
    
    while True:
        
        print(p, i ,j, nums[p - i] + nums[p] + nums[p + j], nums)
        
        if [nums[p - i], nums[p], nums[p + j]] in ans:
            break
        
        if nums[p - i] + nums[p] + nums[p + j] == 0:
            ans.append([nums[p - i], nums[p], nums[p + j]])
        
        if nums[p - i] + nums[p] + nums[p + j] < 0:
            if p + j >= len(nums) - 1:
                break
                
            j += 1
        
        if nums[p - i] + nums[p] + nums[p + j] > 0:
            if p - i <= 0:
                break
                
            i += 1
        

print(ans)