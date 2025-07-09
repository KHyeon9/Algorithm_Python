for i in range(1, int(input()) + 1):
    n, x = map(int, input().split())
    print(f"Case {i}: {n % x}")