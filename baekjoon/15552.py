"""
input은 str로 들어온다.
print(f'{변수명}')으로 js의 `${변수명}`과 같이 쓸 수 있다.
map(lambda x:x*2, iterable)은 map객체 반환

a = map(int, input().split(' '))
b = map(lambda x: x+2, a)

input() 보다 sys.stdin.readline()이 빠르다.

for i in iterable:
for index, i in enumerate(iterable, startIndex?):
ex) list, range(from, to?)
"""

import sys

n = int(sys.stdin.readline())

for i in range(n):
    a, b = map(int, sys.stdin.readline().split(' '))
    print(a + b)
