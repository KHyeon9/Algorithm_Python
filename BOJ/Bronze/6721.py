for _ in range(int(input())):
    a, b = input().split()
    a = int(a[::-1])
    b = int(b[::-1])
    res = str(a + b)[::-1]
    print(int(res))