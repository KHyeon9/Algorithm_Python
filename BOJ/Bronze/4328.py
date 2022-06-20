while 1:
    li = list(map(int, input().split()))
    if li[0] == 0:
        break
    b, p, m = li
    num = int(str(p), b) % int(str(m), b)
    result = []
    while num >= b:
        result.append(num % b)
        num //= b
    result.append(num)
    print(*result[::-1], sep='')
