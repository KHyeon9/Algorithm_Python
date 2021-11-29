for _ in range(int(input())):
    num = input()
    r = str(int(num) + int(num[::-1]))
    if r[::-1] == r:
        print('YES')
    else:
        print('NO')