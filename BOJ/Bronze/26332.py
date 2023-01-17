for _ in range(int(input())):
    n, p = map(int, input().split())
    print(n, p)
    print(n * p - (n - 1) * 2)