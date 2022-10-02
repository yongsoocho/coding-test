from datetime import datetime
from itertools import combinations, permutations


def playGround():
    a = [1,2,3,4]
    print(list(combinations(a, 2)))
    print(type(sum(a)))


start = datetime.now()

playGround()

end = datetime.now()

print(f'{end - start}')

a = [1, 2, 3]

b, c, e = a

print(b, c, e)

# d = [1 ,2, 3]
# if d[3]:
#     print('if')
# else:
#     print('else')


strr = ""

if strr:
    print("if str")
else:
    print('else str')


test_code = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
test_ans = 0

for v in test_code:
    test_ans += max(v)

print(test_ans)