for _ in range(int(input())):
    h, w, n = list(map(int, input().split()))
    num = n // h
    f = h * 100
    if n % h != 0:
        num = n // h + 1
        f = n % h * 100
    print(f + num)
