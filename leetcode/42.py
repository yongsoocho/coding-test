walls = list(map(int, input().strip().split(",")))

left, right = 0, len(walls) - 1

ml, mr = walls[left], walls[right]

ans = 0

while left < right: 
    
    if ml <= mr:
        left += 1
        ml = max(ml, walls[left])
        
        if min(ml, mr) > walls[left]:
            ans += min(ml, mr) - walls[left]
        
    if ml > mr:
        right -= 1
        mr = max(mr, walls[right])
        
        if min(ml, mr) > walls[right]:
            ans += min(ml, mr) - walls[right]
        
    
print(ans)
    