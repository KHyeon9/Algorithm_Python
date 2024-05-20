for i in range(1, int(input()) + 1):
    n, k, s = map(int, input().split())

    print(f"Case #{i}: {n + k + min(0, k - s * 2)}")