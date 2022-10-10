palin = input().strip().split("->")


def solution():
    global palin
    left, right = 0, len(palin) - 1

    while left < right:
        if palin[left] != palin[right]:
            return False

        left += 1
        right -= 1

    return True


print(solution())
