from sys import stdin

N, L = map(int, stdin.readline().strip().split())

x = list(map(int, stdin.readline().strip().split()))
x.sort()
pointer = x[0]

result = 0

for val in x:
    if pointer <= val:
        pointer = val
        result += 1
        pointer += L


print(result)

# from sys import stdin
#
# N, L = map(int, stdin.readline().strip().split())
# coord = [False] * 1001
# for i in map(int, stdin.readline().strip().split()):
#     coord[i] = True
#
# result = 0
# x = 0
#
# while x < 1001:
#     if coord[x]:
#         result += 1
#         x += L
#     else:
#         x += 1
#
# print(result)
