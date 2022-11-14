for t in range(int(input())):
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(1, n - 1):
        if h[i] > (h[i - 1] + h[i + 1]) / 2:
            h[i] = (h[i - 1] + h[i + 1]) / 2
    print("Case #%d: %06f" %((t + 1), h[-2]))