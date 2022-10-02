from sys import stdin

# stack = []
# ans = []

# for c in stdin.readline().strip():
#     stack.append(c)
    
# while stack:
#     ans.append(stack.pop())
    
# print(ans)

arr = list(stdin.readline().strip())

left, right = 0, len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
    
print(arr)