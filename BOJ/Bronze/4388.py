def sol(x, y):
    return x % (10 ** (y + 1)) // (10 ** y)
while 1:
    carry, u = 0, 0
    a, b = map(int, input().split())
    if a == b == 0:
        break
    for i in range(len(str(max(a, b)))):
        n1, n2 = sol(a, i), sol(b, i)
        if n1 + n2 + u >= 10:
            carry += 1
            u = 1
    print(carry)