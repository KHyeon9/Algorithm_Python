while True:
    n, d = map(int, input().split())

    if n == d == 0:
        break

    attend = [0] * n

    for _ in range(d):
        x = list(map(int, input().split()))
        for i in range(n):
            if x[i]:
                attend[i] += 1

    print("yes" if d in attend else "no")