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

