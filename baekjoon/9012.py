# from sys import stdin
#
#
# n = int(stdin.readline().strip())
#
# brackets = []
# stack = []
#
# for i in range(n):
#     brackets.append(stdin.readline().strip())
#
#
# for bracket in brackets:
#     for i in range(len(bracket)):
#         if bracket[i] == '(':
#             stack.append(bracket[i])
#         elif bracket[i] == ')':
#             if not len(stack):
#                 print("NO")
#                 break
#             else:
#                 stack.pop()
#
#         if not len(stack) and i == len(bracket) - 1:
#             print("YES")
#             stack.clear()
#         elif len(stack) and i == len(bracket) - 1:
#             print("NO")
#             stack.clear()

from sys import stdin

brackets = []
stack = []

for _ in range(int(stdin.readline().strip())):
    brackets.append(stdin.readline().strip())


for bracket in brackets:
    result = True

    for ch in bracket:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if not len(stack):
                result = False
                break
            else:
                stack.pop()

    if len(stack):
        result = False

    print("YES" if result else "NO")
    stack.clear()
