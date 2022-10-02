from bisect import bisect_left, bisect_right

from bisect import bisect_left, bisect_right

nums = [0,1,2,3,4,5,6,7,8,9]
n = 5

print(bisect_left(nums, n))
print(bisect_right(nums, n))

print(bisect_left(nums, -3)) # 0
print(bisect_right(nums, -3)) # 0

print(bisect_left(nums, 20)) # 10
print(bisect_right(nums, 20)) # 10

print(bisect_left(nums, 9)) # 9
print(bisect_right(nums, 9)) # 10

print(bisect_left(nums, 0)) # 0
print(bisect_right(nums, 0)) # 1
