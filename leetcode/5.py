strr = input().strip()

left = 0
right = len(strr) - 1
ans = 1

def expanded(i):
    global ans
    
    while True:
        j = 1
        
        if strr[i - j] != strr[i + j]:
            break  
            
        ans +=  1
        
        
    
    return total 

while left < right:
    