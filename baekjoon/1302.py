from sys import stdin

books = dict()

for _ in range(int(stdin.readline().strip())):
    bookName = stdin.readline().strip()
    books[bookName] = books[bookName] + 1 if bookName in books else 1

# sort(iteralbe, key, reverse) 가 나오는데 key 에 - 를 붙여 내림차/오름차로 만들었다. reverse는 내림차를 말함
print(sorted(books.items(), key=lambda item: (-item[1], item[0]))[0][0])

