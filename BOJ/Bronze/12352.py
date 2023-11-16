for t in range(int(input())):
    n = int(input())
    bush = list(map(int, input().split()))

    for i in range(1, n - 1):
        if bush[i] > (bush[i - 1] + bush[i + 1]) / 2:
            bush[i] = (bush[i - 1] + bush[i + 1]) / 2

    print(f"Case #{t + 1}: {bush[-2]:6f}")