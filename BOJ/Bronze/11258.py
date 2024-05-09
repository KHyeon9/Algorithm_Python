lotto = [list(input().split()) for _ in range(6)]

while True:
    num = input()

    if num == "-1":
        break

    res = 0

    if num == lotto[0][0]:
        res += int(lotto[0][1])

    if num[:3] == lotto[1][0]:
        res += int(lotto[1][1])
    elif num[:3] == lotto[2][0]:
        res += int(lotto[2][1])

    if num[3:] == lotto[3][0]:
        res += int(lotto[3][1])
    elif num[3:] == lotto[4][0]:
        res += int(lotto[4][1])

    if num[4:] == lotto[5][0]:
        res += int(lotto[5][1])

    print(res)