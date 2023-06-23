while True:
    n, m = map(int, input().split())

    if n == m == 0:
        break

    total_points = [0] * n

    for _ in range(m):
        points = list(map(int, input().split()))

        for i in range(n):
            total_points[i] += points[i]

    print(max(total_points))
