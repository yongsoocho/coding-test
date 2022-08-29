"""
python은 구조분해 할당이 된다.
a, b = (1, 2)  a, b에 각각 1, 2가 들어간다.
d, c = [1, "2"] type(a)는 int, type(b)는 str이다.

map(적용할 함수 = int(), 반복 가능한 자료 = input().split(' '))
=> 각각의 자료형에 함수를 적용하여 반환해줌
"""


a, b = map(int, input().split(' '))
print(a + b)
