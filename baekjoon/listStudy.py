from datetime import datetime
# import datetime시 datetime.datetime.now()여야 한다.

startAppend = datetime.now()
arr1 = [x * y for x in range(1, 5) for y in range(1, 5)]
add1 = [x * y for x in range(1, 5) for y in range(1, 5)]
arr1.append(add1)
print(arr1)
endAppend = datetime.now()

startSlice = datetime.now()
arr2 = [x * y for x in range(1, 5) for y in range(1, 5)]
add2 = [x * y for x in range(1, 5) for y in range(1, 5)]
arr2.extend(add2)
print(arr2)
endSlice = datetime.now()

# 평균적으로 extend()가 더빠름
print(f"{endAppend - startAppend} ### {endSlice - startSlice}")
