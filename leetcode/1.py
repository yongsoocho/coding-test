def solution():
    nums = map(int, input().strip().split(","))
    target = int(input().strip())

    table = {}

    # 딕셔너리로 저장
    for idx, num in enumerate(nums):
        table[num] = idx

    print(table)    

    # 키로 조회
    for idx, num in enumerate(nums):
        if target - num in table and idx != table[target - num]:
            return idx, table[target - num]


print(solution())
        