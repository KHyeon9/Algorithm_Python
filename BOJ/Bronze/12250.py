for t in range(int(input())):
    a, b, k = map(int, input().split())
    res = 0

    for i in range(a):
        for j in range(b):
            if i & j < k:
                res += 1

    print(f"Case #{t + 1}: {res}")

