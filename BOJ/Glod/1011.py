for _ in range(int(input())):
    x, y = map(int, input().split())
    l = y - x
    cnt = 0
    num = 0
    r = 0
    while 1:
        if r >= l:
            break
        num += 1
        if num % 2 == 1:
            cnt += 1
        r += cnt
    print(num)